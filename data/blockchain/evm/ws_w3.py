from eth_abi import decode
from typing import List, Callable
from web3 import AsyncWeb3, WebSocketProvider
from web3.eth import AsyncEth

class WSProvider(AsyncEth):
    def __init__(self, rpc: str):
        super().__init__(AsyncWeb3())
        self.provider = self.create_provider(rpc)

    def create_provider(self, rpc):
        return AsyncWeb3(WebSocketProvider(rpc))

    async def subscribe(self, events: List[str], contract_addresses: List[str], callback: Callable):
        async with self.provider as w3:
            for contract_address in contract_addresses:
                topics = [w3.keccak(text=event) for event in events]
                filter_params = {
                    "address": contract_address,
                    "topics": topics,
                }
                await w3.eth.subscribe("logs", filter_params)

            async for payload in w3.socket.process_subscriptions():
                await callback(payload)
