from src.database import SistemaDeLogin, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

Session = sessionmaker(engine)

def insert_new_register_in_db(values: dict) -> None:
    with Session() as session:
        insert = SistemaDeLogin(
            login=values['-USER_REGISTER-'],
            password=values['-PASS_REGISTER-']
        )
        session.add(insert)
        session.commit()

def get_password(values: dict) -> str:
    stmt = select(SistemaDeLogin).where(
        SistemaDeLogin.login==values['-USER-']
        )
    with Session() as session:
        result = session.scalars(stmt).first()
        result = result.password
        return result
