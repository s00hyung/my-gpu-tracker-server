import requests, math
from bs4 import BeautifulSoup
from dotenv import dotenv_values
from . import constants

production = True

if production:
    import os

    SERVER_URL = os.environ["SERVER_URL"]
else:
    config = dotenv_values(".env")
    un = config["MONGO_DB_USERNAME"]
    pw = config["MONGO_DB_PASSWORD"]
    url = config["MONGO_DB_URL"]


def find_average(l: list):
    return math.floor(sum(l) / len(l))


async def extract_and_return_price(url: str) -> str:
    try:
        req = await requests.get(url)
        soup = await BeautifulSoup(req.text, features="html.parser")
        # <em class="lowestPrice_num__3AlQ-">1,356,060</em>
        selected = soup.select("div > em")[0]
        # 1,356,060
        return selected.text.replace(",", "")
    except:
        return None


async def start():
    for gpu in constants.ALL_GPUS_DEV:
        average_price = find_average(
            [int(await extract_and_return_price(link)) for link in gpu["links"]]
        )
        params = {"id": gpu["id"]}
        data = {"value": average_price, "currency": "KRW"}
        await requests.post(SERVER_URL, params=params, json=data)


if __name__ == "__main__":
    start()
