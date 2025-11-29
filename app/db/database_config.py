import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

# getting database url using .env 
DATABASEURL = os.getenv("DB_URL")

# creating engine with the database url
engine = create_engine(DATABASEURL, echo=True)

# creating a local session 
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

# function that gets the active local session
def get_db():

    db: Session = SessionLocal()

    try:
        yield db

    finally:
        db.close()


class Base(DeclarativeBase):
    pass
