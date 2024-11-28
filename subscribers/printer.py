from domain.general.subscriber import Subscriber


class Printer(Subscriber):
    def __init__(self):
        super().__init__()

    async def receive(self, event_type: str, event: dict):
        print(event_type, event)
