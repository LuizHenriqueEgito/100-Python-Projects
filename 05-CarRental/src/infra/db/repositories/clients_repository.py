from datetime import datetime
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.clients import Clients as ClientsEntity
from src.data.interfaces.clients_repository import ClientRepositoryInterface
from src.domain.models.clients import Clients

class ClientsRepository(ClientRepositoryInterface):

    @classmethod
    def insert_client(
        cls,
        first_name: str,
        last_name: str,
        cpf: str,
        address: str,
        telephone: str,
        birth_date: str
    ) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = ClientsEntity(
                    first_name=first_name,
                    last_name=last_name,
                    cpf=cpf,
                    address=address,
                    telephone=telephone,
                    birth_date=birth_date
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            

    @classmethod
    def select_client(
        cls,
        cpf
    ) -> list[Clients]:
        with DBConnectionHandler() as database:
            try:
                client = (
                    database.session
                        .query(ClientsEntity)
                        .filter(ClientsEntity.cpf == cpf)
                        .all()
                )
                return client
            except Exception as exception:
                database.session.rollback()
                raise exception