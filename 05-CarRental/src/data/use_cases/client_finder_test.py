from src.infra.db.tests.clients_repository import ClientsRepositorySpy
from .client_finder import ClientFinder

def test_find():
    cpf = '123_ABC'
    repo = ClientsRepositorySpy()
    client_finder = ClientFinder(repo)
    response = client_finder.find(cpf)

    print(response)
    assert response['type'] == 'Clients'
    assert response['count'] == len(response['attributes'])
    assert response['attributes'] != [] 