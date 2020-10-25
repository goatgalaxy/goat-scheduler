import logging
import asyncio

from scheduler.clients import twitter_client, internal_api_client

logger = logging.getLogger(__name__)


def generate_payload(tweet):
    tweet = tweet.AsDict()
    return {
        "message": tweet["text"],
        "region": "USA"
    }

def generate_payload_list(tweets):
    return [generate_payload(tweet) for tweet in tweets]

def get_tweets():
    tweets = twitter_client.GetSearch(
        raw_query="q=twitter%20&result_type=recent&since=2020-10-01&lang=en&count=100"
    )
    return tweets

def publish_payloads(payloads):
    # tasks = [internal_api_client.save_tweet(payload) for payload in payloads]
    # await asyncio.gather(*tasks)
    i = 0
    for payload in payloads:
        internal_api_client.save_tweet(payload) 
        logger.info(f"{i} - {payload}")
        i += 1

async def handle():
    tweets = get_tweets()
    payloads = generate_payload_list(tweets)
    logger.info(payloads)
    publish_payloads(payloads)
    logger.info("Tweets saved in the internal api")
    return True
