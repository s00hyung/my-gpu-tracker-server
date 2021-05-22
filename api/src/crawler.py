import requests, json
from utilities import constants, functions
from bs4 import BeautifulSoup
from collections import defaultdict


def build_prices_list():
    final_list = []
    for gpu in constants.ALL_GPUS:
        new_dict = {}
        new_dict["name"] = gpu["name"]
        new_dict["prices"] = []

        for link in gpu["links"]:
            price = extract_and_return_price(link)
            if price:
                new_dict["prices"].append(int(price))
            else:
                pass
        new_dict["average_price"] = functions.find_average(new_dict["prices"])
        final_list.append(new_dict)
    return final_list


def extract_and_return_price(url: str) -> str:

    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text)
        # <em class="lowestPrice_num__3AlQ-">1,356,060</em>
        selected = soup.select("div > em")[0]
        # 1,356,060
        return selected.text.replace(",", "")
    except:
        return None


def read_json():
    json_dict = {}
    with open(constants.JSON_DIR, "r") as json_file:
        json_dict = json.load(json_file)
    return json_dict


def write_json(final_list, json_dict):
    today_date = functions.get_today_date()
    json_dict[today_date] = final_list

    try:
        with open(constants.JSON_DIR, "w") as json_file:
            json.dump(json_dict, json_file)
    except:
        print("Failed to write JSON file")
    else:
        print("Sucessfully wrote JSON file")


def start():
    final_list = build_prices_list()
    json_dict = {}
    try:
        json_dict = read_json()
    except FileNotFoundError:
        write_json(final_list, defaultdict(functions.nested_dict))
    else:
        write_json(final_list, json_dict)


start()
