from data.blockchain.evm.type import EventRequestDTO, SubscribeRequestDTO
from data.blockchain.evm.w3 import Provider
from data.blockchain.evm.ws_w3 import WSProvider
from domain.general.blockchain import Blockchain


class EVM(Blockchain):
    def __init__(self, provider: Provider, ws_provider: WSProvider):
        self.provider = provider
        self.ws_provider = ws_provider

    async def send_transaction(self, data: dict):
        pass

    async def get_data(self, data: dict):
        method = data.get("method")
        if method == "events":
            return await self._get_events(EventRequestDTO(**data))
        elif method == "subscribe":
            return await self._subscribe(SubscribeRequestDTO(**data))
        else:
            raise Exception(f"Method {method} not found")

    async def _get_events(self, data: EventRequestDTO):
        params = {
            "address": data.get("address"),
            "fromBlock": data.get("from_block"),
            "toBlock": data.get("to_block"),
            "topics": [
                self.ws_provider.provider.keccak(text=topic)
                for topic in data.get("topics")
            ],
        }

        print(params)

        return await self.provider.get_logs(params)

    async def _subscribe(self, data: SubscribeRequestDTO):
        events = data.get("events")
        addresses = data.get("addresses")
        callback = data.get("callback")

        await self.ws_provider.subscribe(events, addresses, callback)
