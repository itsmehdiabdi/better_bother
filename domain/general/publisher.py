from typing import List, Dict, Generic, TypeVar

from domain.general.subscriber import Subscriber

EventType = TypeVar("EventType")


class Publisher(Generic[EventType]):
    subscribers: Dict[EventType, List[Subscriber]] = {}

    def subscribe(self, event: EventType, subscriber: Subscriber):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(subscriber)

    async def publish(self, event: EventType, data: dict):
        for subscriber in self.subscribers.get(event, []):
            await subscriber.receive(event, data)
