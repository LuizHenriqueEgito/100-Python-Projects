from .clients_repository import ClientsRepository

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