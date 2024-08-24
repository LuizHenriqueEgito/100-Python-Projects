from src.domain.use_case.client_finder import ClientFinder as ClientFinderInterface
from src.data.interfaces.clients_repository import ClientRepositoryInterface

class ClientFinder(ClientFinderInterface):
    def __init__(self, clients_repository: ClientRepositoryInterface) -> None:
        self.__clients_repository = clients_repository

    def find(self, cpf: str) -> dict:
        pass