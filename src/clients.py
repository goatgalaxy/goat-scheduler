import twitter
from config import settings

twitter_api = twitter.Api(
    consumer_key=settings.CONSUMER_KEY,
    consumer_secret=settings.CONSUMER_SECRET,
    access_token_key=settings.ACCESS_TOKEN_KEY,
    access_token_secret=settings.ACCESS_TOKEN_SECRET)
