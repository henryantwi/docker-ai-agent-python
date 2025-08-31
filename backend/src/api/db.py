import os 

from sqlmodel import create_engine, Session, SQLModel

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)


def init_db():
    print("creating database tables...")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
        