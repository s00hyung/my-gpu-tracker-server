import math, pytz
from datetime import datetime
from collections import defaultdict
from . import constants


def get_today_date():
    return str(datetime.today().strftime("%Y-%m-%d"))


def get_current_time():
    tz = pytz.timezone(constants.TZ)
    return str(datetime.now(tz).strftime("%Y-%m-%d-%H:%M:%S"))


def nested_dict():
    return defaultdict(nested_dict)


def find_average(l: list):
    return math.floor(sum(l) / len(l))
