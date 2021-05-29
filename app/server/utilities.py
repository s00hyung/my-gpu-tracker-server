import pytz, configparser
from datetime import datetime

config = configparser.ConfigParser()
config.read("conf.ini")

TIMEZONE = config["DATE"]["tz"]
tz = pytz.timezone(TIMEZONE)


def get_today_date() -> str:
    return str(datetime.now(tz).strftime("%Y-%m-%d"))


def get_current_time() -> datetime:
    return datetime.now(tz)
