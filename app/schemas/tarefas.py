from pydantic import BaseModel
from typing import Optional


class TarefaBase(BaseModel):
    titulo: str
    status: str


class TarefaCreate(TarefaBase):
    """Create Tarefa schema"""


class TarefaRead(TarefaBase):
    id: int
    projeto_id: int

    class Config:
        orm_mode = True


class TarefaUpdate(BaseModel):
    titulo: Optional[str]
    status: Optional[str]
