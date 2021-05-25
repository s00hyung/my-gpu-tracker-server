import requests, json, logging
from bs4 import BeautifulSoup
from collections import defaultdict
from . import constants, functions


def build_prices_list():
    final_list = []

    for gpu in constants.ALL_GPUS:
        logging.warning(f"Pulling prices of {gpu['name']}...")
        new_dict = {}
        new_dict["name"] = gpu["name"]
        new_dict["prices"] = []

        for i, link in enumerate(gpu["links"]):
            price = extract_and_return_price(link)
            if price:
                logging.warning(f"[{i+1}] {price} KRW")
                new_dict["prices"].append(int(price))
            else:
                pass
        new_dict["average_price"] = functions.find_average(new_dict["prices"])
        final_list.append(new_dict)
    return final_list


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


def read_json():
    logging.warning("Loading existing JSON file...")
    json_dict = {}
    with open(constants.JSON_DIR, "r") as json_file:
        json_dict = json.load(json_file)
    return json_dict


def write_json(final_list, json_dict):
    today_date = functions.get_today_date()
    json_dict["last-updated"] = functions.get_current_time()
    json_dict[today_date] = final_list

    try:
        with open(constants.JSON_DIR, "w") as json_file:
            json.dump(json_dict, json_file, indent=4, sort_keys=True)
    except:
        logging.warning("Failed to write JSON file.")
    else:
        logging.warning("Sucessfully wrote JSON file.")


def start_crawl():
    logging.warning("----- Initiating Crawling -----")
    final_list = build_prices_list()
    json_dict = {}
    try:
        json_dict = read_json()
    except FileNotFoundError:
        logging.warning("Existing JSON file not found!")
        logging.warning("Writting new JSON file...")
        write_json(final_list, defaultdict(functions.nested_dict))
    else:
        logging.warning("Updating existing JSON file.")
        write_json(final_list, json_dict)

    logging.warning("----- Finisehd Crawling -----")


if __name__ == "__main__":
    start_crawl()
