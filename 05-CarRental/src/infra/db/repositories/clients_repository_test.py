from sqlalchemy import text
from .clients_repository import ClientsRepository
from src.infra.db.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect() 


def test_insert_client():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_cpf = 'cpf_1'
    mocked_address = 'address'
    mocked_telephone = 'telephone'
    mocked_birth_date = '1997-04-07'

    client_repository = ClientsRepository()
    client_repository.insert_client(
        mocked_first_name,
        mocked_last_name,
        mocked_cpf,
        mocked_address,
        mocked_telephone,
        mocked_birth_date
    )


def test_select_client():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_cpf = 'cpf_3'
    mocked_address = 'address'
    mocked_telephone = 'telephone'
    mocked_birth_date = '1997-04-07'
    sql = '''
        INSERT INTO CLIENTS (first_name, last_name, cpf, address, telephone, birth_date) 
        VALUES ('{}', '{}',  '{}', '{}', '{}', '{}')
    '''.format(mocked_first_name, mocked_last_name, mocked_cpf, mocked_address, mocked_telephone, mocked_birth_date)
    connection.execute(text(sql))
    connection.commit()


    client_repository = ClientsRepository()
    response = client_repository.select_client(mocked_cpf)
    print(response[0])
    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name

    connection.execute(text(f'''DELETE FROM CLIENTS WHERE ID={response[0].id}'''))
    connection.commit() 