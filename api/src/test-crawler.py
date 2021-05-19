import requests, json
from bs4 import BeautifulSoup
from datetime import datetime
from collections import defaultdict


def get_today_date():
    return str(datetime.today().strftime("%Y-%m-%d"))


def nested_dict():
    return defaultdict(nested_dict)


product_code = "24715289522"
url = f"https://search.shopping.naver.com/catalog/{product_code}"

req = requests.get(url)
soup = BeautifulSoup(req.text)

# <em class="lowestPrice_num__3AlQ-">1,356,060</em>
selected = soup.select("div > em")[0]

# 1,356,060
print(selected.text)

today_date = get_today_date()
data_in_json = defaultdict(nested_dict)
data_in_json[today_date][product_code]["price"] = selected.text.replace(",", "")

with open("price_list.json", "w") as json_file:
    json.dump(data_in_json, json_file)
