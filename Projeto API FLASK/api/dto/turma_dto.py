from datetime import date
from dataclasses import dataclass

@dataclass
class TurmaDTO(self):
    nome: str
    descricao: str
    data_inicio: date
    data_fim: date