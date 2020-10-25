import json
import requests

import twitter


from scheduler.config import settings

class InternalTwitterApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def save_tweet(self, body, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = f"{self.base_url}/tweet/"
        data = json.dumps(body)
        requests.post(url, data=data, headers=headers)


twitter_client = twitter.Api(
    consumer_key=settings.CONSUMER_KEY,
    consumer_secret=settings.CONSUMER_SECRET,
    access_token_key=settings.ACCESS_TOKEN_KEY,
    access_token_secret=settings.ACCESS_TOKEN_SECRET
)

internal_api_client = InternalTwitterApiClient(settings.API_URL)

