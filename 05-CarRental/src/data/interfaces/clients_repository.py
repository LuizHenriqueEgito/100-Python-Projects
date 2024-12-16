
from abc import ABC, abstractmethod
from src.domain.models.clients import Clients

class ClientRepositoryInterface(ABC):
    @classmethod
    @abstractmethod
    def insert_client(self, first_name: str, last_name: str, cpf: str, address: str, telephone: str, birth_date: str) -> None: pass
    
    @classmethod
    @abstractmethod
    def select_client(self, cpf: str) -> list[Clients]: pass