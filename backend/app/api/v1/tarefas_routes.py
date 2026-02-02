from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.tarefas import TarefaCreate, TarefaRead, TarefaUpdate
from app.services.tarefas import (
    get_tarefa_by_id,
    create_tarefa,
    delete_tarefa,
    update_tarefa,
    get_all_tarefas,
)
from app.db.database_config import get_db, Session

router = APIRouter(prefix="/v1/tarefas", tags=["Tarefas"])


@router.post(
    "/projeto/{projeto_id}", response_model=TarefaRead, status_code=status.HTTP_200_OK
)
def create_new_tarefa(
    tarefa: TarefaCreate, projeto_id: int, db: Session = Depends(get_db)
):

    return create_tarefa(db, tarefa, projeto_id)


@router.get("/", response_model=list[TarefaRead], status_code=status.HTTP_200_OK)
def get_tarefas(db: Session = Depends(get_db)):

    return get_all_tarefas(db)


@router.get(
    "/{tarefa_id}/projeto/{projeto_id}",
    response_model=TarefaRead,
    status_code=status.HTTP_200_OK,
)
def get_tarefa(tarefa_id: int, projeto_id: int, db: Session = Depends(get_db)):

    return get_tarefa_by_id(db, tarefa_id, projeto_id)


@router.put(
    "/{tarefa_id}/projeto/{projeto_id}",
    response_model=TarefaRead,
    status_code=status.HTTP_200_OK,
)
def update_tarefa_by_id(
    tarefa_id: int,
    tarefa: TarefaUpdate,
    projeto_id: int,
    db: Session = Depends(get_db),
):

    updated = update_tarefa(db, tarefa_id, projeto_id, tarefa)

    return updated


@router.delete(
    "/{tarefa_id}/projeto/{projeto_id}",
    response_model=TarefaRead,
    status_code=status.HTTP_200_OK,
)
def delete_tarefa_by_id(tarefa_id, projeto_id: int, db: Session = Depends(get_db)):

    deleted = delete_tarefa(db, tarefa_id, projeto_id)

    return deleted
