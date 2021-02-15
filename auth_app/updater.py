from apscheduler.schedulers.background import BackgroundScheduler
from .link_checker import check_links_in_db


def check_links_scheduller():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_links_in_db, 'interval', hours=2)
    scheduler.start()

