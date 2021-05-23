import sys

sys.path.insert(0, "src")

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import src.crawler as crawlers


sched = AsyncIOScheduler()


@sched.scheduled_job("cron", day_of_week="mon-sun", hour=23)
def scheduled_job():
    crawler.start()


sched.start()
