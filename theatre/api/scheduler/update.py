from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import forecastApi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedulerApi.MovieRangeDelete, 'interval', minutes=1)
    scheduler.start()