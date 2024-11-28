import asyncio
from data.blockchain.evm.base import EVM
from data.blockchain.evm.w3 import Provider
from data.blockchain.evm.ws_w3 import WSProvider
from publishers.uniswap_event.base import UniswapSwapPublisher
from subscribers.printer import Printer

w3_provider = Provider(["https://eth.drpc.org"])
ws_provider = WSProvider("wss://ethereum-rpc.publicnode.com")
evm = EVM(provider=w3_provider, ws_provider=ws_provider)

contracts = ["0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc"]
users = ["0x0000000000000000000000000000000000000000"]
uniswap_swap_publisher = UniswapSwapPublisher(evm, contracts, users)

printer = Printer()

uniswap_swap_publisher.subscribe(event="swap", subscriber=printer)

asyncio.run(uniswap_swap_publisher.listen_for_swaps())
