from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    async def receive(self, event_type: str, event: dict):
        raise NotImplementedError
