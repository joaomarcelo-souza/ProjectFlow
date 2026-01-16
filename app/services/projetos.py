from sqlalchemy.orm import Session
from app.schemas.projetos import ProjetoCreate, ProjetoUpdate
from app.models.projetos import Projeto


def create_projeto(db: Session, projeto_data: ProjetoCreate) -> Projeto:

    projeto = Projeto(**projeto_data.model_dump())

    db.add(projeto)
    db.commit()
    db.refresh(projeto)

    return projeto


def get_all_projetos(db: Session):

    projetos = db.query(Projeto).all()

    return projetos


def get_projeto_by_id(db: Session, projeto_id: int):

    projeto = db.query(Projeto).filter(Projeto.id == projeto_id).first()

    return projeto


def update_projeto(db: Session, projeto_id: int, projeto_data: ProjetoUpdate):

    projeto = get_projeto_by_id(db, projeto_id)

    if projeto:

        for field, value in projeto_data.model_dump(exclude_unset=True).items():
            setattr(projeto, field, value)

        db.commit()
        db.refresh(projeto)

    return projeto


def delete_projeto(db: Session, projeto_id: int):

    projeto = get_projeto_by_id(db, projeto_id)

    if projeto:

        db.delete(projeto)
        db.commit()

    return projeto
