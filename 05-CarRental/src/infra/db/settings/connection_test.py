# from sqlalchemy import text
import pytest
from .connection import DBConnectionHandler


@pytest.mark.skip(reason='Sensitive test')
def test_create_database_engine():
    db_connection_handle = DBConnectionHandler()
    engine = db_connection_handle.get_engine()
    assert engine is not None
    # print('\n'*5)
    # print(engine)
    # conn = engine.connect()

    # conn.execute(
    #     text("INSERT INTO CLIENTS (FIRST_NAME, LAST_NAME, CPF, ADDRESS, TELEPHONE, BIRTH_DATE) VALUES ('LUIZ', 'HENRIQUE', '4333333333', 'SAO PAULO', '1199999999', '1997-04-07')")
    # )
    # conn.commit()

