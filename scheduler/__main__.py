import asyncio
import logging
from concurrent.futures import CancelledError

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler.config import settings
from scheduler.jobs import create_new_tweets

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Initilizaing scheduler")

scheduler = AsyncIOScheduler()

scheduler.add_job(
    func=create_new_tweets.handle,
    trigger="interval",
    minutes=settings.SERVICE_SCHEDULED_TIME,
    max_instances=10,
)

scheduler.start()

loop = asyncio.get_event_loop()
try:
    loop.run_forever()
except CancelledError:
    loop.close()