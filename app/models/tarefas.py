from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db.database_config import Base


class Tarefa(Base):

    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False, default="pendente")
    projeto_id: Mapped[int] = mapped_column(ForeignKey("projetos.id"))

    projeto: Mapped["Projeto"] = relationship(back_populates="tarefas")

    __table_args__ = (
        UniqueConstraint("projeto_id", "titulo", name="uq_tarefa_projeto_titulo"),
    )


from app.models.projetos import Projeto
