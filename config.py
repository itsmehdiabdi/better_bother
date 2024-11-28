import os
from dotenv import load_dotenv
from domain.utils.singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.load_env()

    def load_env(self):
        load_dotenv()
        self.redis_url = os.getenv("REDIS_URL")
