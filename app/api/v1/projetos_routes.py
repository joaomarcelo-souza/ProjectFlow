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

    created = create_projeto(db, projeto)

    if not created:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return created


@router.get("/", response_model=list[ProjetoRead], status_code=status.HTTP_200_OK)
def get_projetos(db: Session = Depends(get_db)):

    return get_all_projetos(db)


@router.get("/{projeto_id}", response_model=ProjetoRead, status_code=status.HTTP_200_OK)
def get_projeto(projeto_id: int, db: Session = Depends(get_db)):

    updated = get_projeto_by_id(db, projeto_id)

    if not updated:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="ID não encontrado")

    return updated


@router.put("/{projeto_id}", response_model=ProjetoRead, status_code=status.HTTP_200_OK)
def update_projeto_by_id(
    projeto_id: int, projeto: ProjetoUpdate, db: Session = Depends(get_db)
):

    updated = update_projeto(db, projeto_id, projeto)

    return updated


@router.delete(
    "/{projeto_id}", response_model=ProjetoRead, status_code=status.HTTP_200_OK
)
def delete_projeto_by_id(projeto_id: int, db: Session = Depends(get_db)):

    deleted = delete_projeto(db, projeto_id)

    return deleted
