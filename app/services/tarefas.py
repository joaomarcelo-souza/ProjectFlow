from sqlalchemy.orm import Session
from app.schemas.tarefas import TarefaCreate, TarefaUpdate
from app.models.tarefas import Tarefa


def create_tarefa(db: Session, tarefa_data: TarefaCreate, projeto_id: int) -> Tarefa:

    tarefa = Tarefa(**tarefa_data.model_dump(), projeto_id=projeto_id)

    db.add(tarefa)
    db.commit()
    db.refresh(tarefa)

    return tarefa


def get_all_tarefas(db: Session):

    tarefas = db.query(Tarefa).all()

    return tarefas


def get_tarefa_by_id(db: Session, tarefa_id: int, projeto_id: int):

    tarefa = (
        db.query(Tarefa)
        .filter(Tarefa.id == tarefa_id, Tarefa.projeto_id == projeto_id)
        .first()
    )

    return tarefa


def update_tarefa(
    db: Session, tarefa_id: int, projeto_id: int, tarefa_data: TarefaUpdate
):

    tarefa = get_tarefa_by_id(db, tarefa_id, projeto_id)

    if tarefa:

        for field, value in tarefa_data.model_dump(exclude_unset=True).items():
            setattr(tarefa, field, value)

        db.commit()
        db.refresh(tarefa)

    return tarefa


def delete_tarefa(db: Session, tarefa_id: int, projeto_id: int):

    tarefa = get_tarefa_by_id(db, tarefa_id, projeto_id)

    if tarefa:

        db.delete(tarefa)
        db.commit()

    return tarefa
