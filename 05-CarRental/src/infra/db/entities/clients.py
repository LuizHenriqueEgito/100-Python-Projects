from src.infra.db.settings.base import Base
from sqlalchemy import Column, String, Integer, Date

class Clients(Base):
    __tablename__ = 'CLIENTS'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    address = Column(String, nullable=False)
    telephone = Column(String)
    birth_date = Column(Date)