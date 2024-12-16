from datetime import datetime
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.clients import Clients as ClientsEntity
from src.data.interfaces.clients_repository import ClientRepositoryInterface
from src.domain.models.clients import Clients

class ClientsRepositorySpy():

    def __init__(self) -> None:
        self.insert_client_attributes = {}
        self.select_client_attributes = {}

    def insert_client(
        self,
        first_name: str,
        last_name: str,
        cpf: str,
        address: str,
        telephone: str,
        birth_date: str
    ) -> None:
        self.insert_client_attributes['first_name'] = first_name
        self.insert_client_attributes['last_name'] = last_name
        self.insert_client_attributes['cpf'] = cpf
        self.insert_client_attributes['address'] = address
        self.insert_client_attributes['telephone'] = telephone
        self.insert_client_attributes['birth_date'] = birth_date
        

    def select_client(
        self,
        cpf
    ) -> list[Clients]:
        self.select_client_attributes['cpf'] = cpf
        return [
            Clients(1, 'A', 'B', cpf, 'D', 'E', '2021-04-07'),
            Clients(2, 'Z', 'Y', cpf, 'X', 'W', '2021-09-30')
        ]