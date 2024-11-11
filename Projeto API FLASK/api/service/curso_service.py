from ..models import curso_model
from api import db
from .disciplina_service import listar_disciplinas_by_id

def cadastrar_curso(curso):
    curso_bd = curso_model(nome=curso.nome, descricao=curso.descricao, data_inicio=curso.data_inicio, data_fim=curso.data_fim)
    for i in curso.disciplinas:
        disciplina = listar_disciplinas_by_id(id)
        curso_bd.disciplinas.append(disciplina)

    db.session.add(curso_bd)
    db.session.commit()
    return  curso_bd

def listar_cursos():
    cursos = curso_model.CursoModel.querry.all()
    return cursos

def listar_cursos_by_id(param_id):
    curso = curso_model.CursoModel.querry.filter_by(id=param_id).first()
    return curso

def atualizar_curso(curso_db, curso_atualizada):
    curso_db.nome = curso_atualizada.nome
    curso_db.descricao = curso_atualizada.descricao
    curso_db.data_inicio = curso_atualizada.data_inicio
    curso_db.data_fim = curso_atualizada.data_fim
    curso_db.disciplinas = []
    for i in curso_atualizada.disciplinas:
        disciplina = listar_disciplinas_by_id(id)
        curso_db.disciplinas.append(disciplina)
    db.session.commit()

def excluir_curso(curso):
    db.session.delete(curso)
    db.session.commit()
