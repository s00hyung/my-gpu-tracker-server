import math
from datetime import datetime
from collections import defaultdict


def get_today_date():
    return str(datetime.today().strftime("%Y-%m-%d"))


def nested_dict():
    return defaultdict(nested_dict)


def find_average(l: list):
    return math.floor(sum(l) / len(l))
