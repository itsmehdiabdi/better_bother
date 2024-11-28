from redis import Redis
from domain.general.storage import Storage


class RedisClient(Storage):
    def __init__(self, url: str):
        self.client = Redis(url)

    def save(self, key: str, value: str):
        self.client.set(key, value)

    def load(self, key: str):
        return self.client.get(key)
