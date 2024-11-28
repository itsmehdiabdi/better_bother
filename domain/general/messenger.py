from abc import ABC, abstractmethod

class Messenger(ABC):
    @abstractmethod
    def send(self, message: dict) -> bool:
        raise NotImplementedError

