from ..models import turma_model
from api import db

def cadastrar_turma(turma):
    turma_bd = turma_model(nome=turma.nome, descricao=turma.descricao, data_inicio=turma.data_inicio, data_fim=turma.data_fim)
    db.session.add(turma_bd)
    db.session.commit()
    return  turma_bd

def listar_turmas():
    turmas = turma_model.TurmaModel.querry.all()
    return turmas

def listar_turmas_by_id(param_id):
    turma = turma_model.TurmaModel.querry.filter_by(id=param_id).first()
    return turma

def atualizar_turma(turma_db, turma_atualizada):
    turma_db.nome = turma_atualizada.nome
    turma_db.descricao = turma_atualizada.descricao
    turma_db.data_inicio = turma_atualizada.data_inicio
    turma_db.data_fim = turma_atualizada.data_fim
    db.session.commit()

def excluir_turma(turma):
    db.session.delete(turma)
    db.session.commit()
