import requests, math
from bs4 import BeautifulSoup
from dotenv import dotenv_values


config = dotenv_values(".env")
SERVER_URL = config["SERVER_HOST"]

RTX3090 = {
    "id": "rtx3090",
    "links": [
        "https://search.shopping.naver.com/catalog/24723487523",
        "https://search.shopping.naver.com/catalog/25733875525",
    ],
}

ALL_GPUS_DEV = [
    RTX3090,
]


def find_average(l: list):
    return math.floor(sum(l) / len(l))


def extract_and_return_price(url: str) -> str:
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, features="html.parser")
        # <em class="lowestPrice_num__3AlQ-">1,356,060</em>
        selected = soup.select("div > em")[0]
        # 1,356,060
        return selected.text.replace(",", "")
    except:
        return None


def start():
    for gpu in ALL_GPUS_DEV:
        average_price = find_average(
            [int(extract_and_return_price(link)) for link in gpu["links"]]
        )
        data = {"value": average_price, "currency": "KRW"}
        print(data)
        print(requests.post(f"{SERVER_URL}/?id={gpu['id']}", data))


if __name__ == "__main__":
    start()
