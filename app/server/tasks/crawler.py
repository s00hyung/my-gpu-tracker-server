import requests
from bs4 import BeautifulSoup
from . import constants, functions
from dotenv import dotenv_values

config = dotenv_values(".env")
SERVER_URL = config["SERVER_HOST"]


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
    async for gpu in constants.ALL_GPUS_DEV:
        average_price = await functions.find_average(
            [await extract_and_return_price(link) for link in gpu["links"]]
        )
        data = {"value": average_price, "currency": "KRW"}
        await requests.post(f"{SERVER_URL}/{gpu['id']}", data)


if __name__ == "__main__":
    start()
