import asyncio

from web3 import AsyncHTTPProvider, AsyncWeb3
from web3.eth import AsyncEth
from typing import List


class Provider(AsyncEth):
    def __init__(self, rpcs: List[str]):
        super().__init__(AsyncWeb3())
        self.providers = [self.create_provider(rpc) for rpc in rpcs]

    def create_provider(self, rpc):
        return AsyncWeb3(AsyncHTTPProvider(rpc)).eth

    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if asyncio.iscoroutinefunction(attr):

            async def wrapper(*args, **kwargs):
                return await execute_until_first(self.providers, name, *args, **kwargs)

            return wrapper
        return attr


async def execute_until_first(providers: List[AsyncEth], name: str, *args, **kwargs):
    """
    Executes coroutines in parallel and returns the first successful result

    Args:
        coroutines: List of coroutines to execute

    Returns:
        First successful result from the coroutines
        Raises Exception if all coroutines fail
    """
    exceptions = []
    for provider in providers:
        try:
            result = await getattr(provider, name)(*args, **kwargs)
            return result
        except Exception as e:
            exceptions.append(e)
            continue
    raise Exception(exceptions)
