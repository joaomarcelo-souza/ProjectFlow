from pydantic import BaseModel
from typing import Optional, List
from app.schemas.tarefas import TarefaRead


class ProjetoBase(BaseModel):
    nome: str
    descricao: str


class ProjetoCreate(ProjetoBase):
    """Create Projeto schema"""


class ProjetoRead(ProjetoBase):
    id: int
    tarefas: List[TarefaRead]

    class Config:
        from_attributes = True


class ProjetoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
