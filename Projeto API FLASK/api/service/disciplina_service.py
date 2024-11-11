from api import db
from .. models import disciplina_model

def cadastrar_disciplina(disciplina):
    disciplina_bd = disciplina_model.DisciplinaModel(nome=disciplina.nome)
    db.session.add(disciplina_bd)
    db.session.commit()
    return disciplina_bd

def listar_disciplinas():
    disciplinas = disciplina_model.DisciplinaModel.query.all()
    return disciplinas

def listar_disciplinas_by_id(id):
    disciplinas = disciplina_model.DisciplinaModel.query.filter_by(id=param_id).first()
    return disciplinas

def atualizar_disciplina(disciplina_db, disciplina_atualizada):
    disciplina_db.nome = disciplina_atualizada.nome
    db.session.commit()

def excluir_disciplina(disciplina):
    db.session.delete(disciplina)
    db.session.commit()