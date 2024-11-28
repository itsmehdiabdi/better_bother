from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self, key: str, value: str):
        raise NotImplementedError

    @abstractmethod
    def load(self, key: str):
        raise NotImplementedError
