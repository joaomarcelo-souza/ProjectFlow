from fastapi import FastAPI
from app.db.database_config import Base, engine
from app.api.v1.projetos_routes import router as projetos_router
from app.api.v1.tarefas_routes import router as tarefas_router


app = FastAPI(title="Project Flow")

Base.metadata.create_all(bind=engine)

app.include_router(router=projetos_router)
app.include_router(router=tarefas_router)
