from abc import ABC, abstractmethod

class Blockchain(ABC):
    @abstractmethod
    async def send_transaction(self, data: dict):
        pass
    
    @abstractmethod
    async def get_data(self, data: dict):
        pass

