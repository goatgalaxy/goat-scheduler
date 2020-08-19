from prettyconf import config

class Settings:
    API_URL = config("API_URL")
    CONSUMER_KEY = config("CONSUMER_KEY")
    CONSUMER_SECRET = config("CONSUMER_SECRET")
    ACCESS_TOKEN_KEY = config("ACCESS_TOKEN_KEY")
    ACCESS_TOKEN_SECRET = config("ACCESS_TOKEN_SECRET")

settings = Settings()
