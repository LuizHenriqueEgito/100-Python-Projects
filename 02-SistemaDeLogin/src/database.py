# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy import select
# from sqlalchemy.orm import sessionmaker

from datetime import datetime
from sqlalchemy import func, create_engine
from sqlalchemy.orm import Mapped, mapped_column, registry

reg = registry()
engine = create_engine("sqlite:///02-SistemaDeLogin/db/sistem.db")

@reg.mapped_as_dataclass
class SistemaDeLogin:
    __tablename__ = "sistema_de_login"
    login: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str]
    dt_registration: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )

def create_ifnot_exists() -> None:
    reg.metadata.create_all(bind=engine, checkfirst=True)

