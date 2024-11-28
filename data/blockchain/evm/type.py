from typing import List, Callable, TypedDict


class EventRequestDTO(TypedDict):
    address: str
    topics: List[str]
    from_block: int
    to_block: int


class SubscribeRequestDTO(TypedDict):
    events: List[str]
    addresses: List[str]
    callback: Callable
