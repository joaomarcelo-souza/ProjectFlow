from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.projetos import ProjetoCreate, ProjetoUpdate, ProjetoRead
from app.services.projetos import (
    get_all_projetos,
    get_projeto_by_id,
    update_projeto,
    delete_projeto,
    create_projeto,
)
from app.db.database_config import get_db, Session

router = APIRouter(prefix="/v1/projetos", tags=["Projeto"])


@router.post("/", response_model=ProjetoRead, status_code=status.HTTP_200_OK)
def create_new_projeto(projeto: ProjetoCreate, db: Session = Depends(get_db)):

    return create_projeto(db, projeto)


@router.get("/", response_model=list[ProjetoRead], status_code=status.HTTP_200_OK)
def get_projetos(db: Session = Depends(get_db)):

    return get_all_projetos(db)
