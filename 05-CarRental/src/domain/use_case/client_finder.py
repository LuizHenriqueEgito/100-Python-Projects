from abc import ABC, abstractmethod

class ClientFinder(ABC):
    @classmethod
    @abstractmethod
    def find(self, cpf: str) -> dict: pass


