from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
import time

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

def create_db_engine():
    return create_engine(SQLALCHEMY_DATABASE_URL)

def wait_for_db(engine, retries=5, delay=5):
    for i in range(retries):
        try:
            with engine.connect():
                return True
        except exc.OperationalError:
            if i < retries - 1:
                time.sleep(delay)
                continue
            raise

engine = create_db_engine()
wait_for_db(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()