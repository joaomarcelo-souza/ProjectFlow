from fastapi import FastAPI
from app.db.database_config import Base, engine
from app.api.v1.projetos_routes import router as projetos_router

app = FastAPI(title="Project Flow")

Base.metadata.create_all(bind=engine)

app.include_router(router=projetos_router)
