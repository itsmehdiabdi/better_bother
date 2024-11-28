from typing import List
from domain.general.publisher import Publisher
from data.blockchain.evm.base import EVM
from publishers.uniswap_event.type import UniswapEventType


class UniswapSwapPublisher(Publisher[UniswapEventType]):
    def __init__(self, evm: EVM, token_addresses: List[str], user_addresses: List[str]):
        super().__init__()
        self.evm = evm
        self.token_addresses = token_addresses
        self.user_addresses = user_addresses

    async def listen_for_swaps(self):
        events = ["Swap(address,uint256,uint256,uint256,uint256,address)"]
        await self.evm.get_data({"method": "subscribe", "events": events,
                                 "addresses": self.token_addresses, "callback": self.on_swap})

    async def on_swap(self, payload: dict):
        await self.publish("swap", payload)
