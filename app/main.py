from fastapi import FastAPI
from app.db.database_config import Base, engine

app = FastAPI(title="Project Flow")

Base.metadata.create_all(bind=engine)
