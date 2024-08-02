from sqlmodel import Session, SQLModel, create_engine

from models import *

engine = create_engine("sqlite:///test.db", echo=True)
SQLModel.metadata.create_all(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
