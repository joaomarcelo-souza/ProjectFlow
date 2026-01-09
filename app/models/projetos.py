from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db.database_config import Base


class Projeto(Base):

    __tablename__ = "projetos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    descricao: Mapped[str] = mapped_column(nullable=False)

    tarefas: Mapped[list["Tarefa"]] = relationship(
        back_populates="projeto", cascade="all, delete"
    )


from app.models.tarefas import Tarefa
