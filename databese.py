from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine(
    url = "sqlite:///./test.db",
    echo = False 
)

Session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass


