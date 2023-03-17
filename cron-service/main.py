import time
import schedule
from dotenv import load_dotenv

from settings import NOTIFICATIONS_SERVICE_URL
from requests_common import request_with_retries


def scheduled_notifications():
    request_with_retries(
        "POST",
        url=f"{NOTIFICATIONS_SERVICE_URL}/internal/notifications/scheduled",
    )


def another_task():
    print("Executing another task...")


def setup_cron_tasks():
    schedule.every(10).seconds.do(scheduled_notifications)
    schedule.every().hour.do(another_task)


if __name__ == "__main__":
    load_dotenv()
    setup_cron_tasks()
    while True:
        schedule.run_pending()
        time.sleep(5)
