from datetime import date
from dataclasses import dataclass

@dataclass
class CursoDTO():
    nome: str
    descricao: str
    disciplina: str