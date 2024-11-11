from flask_restful import Resource
from api import api
from ..schemas import disciplina_schema
from flask import request, make_response, jsonify
from ..dto import disciplina_dto
from ..service import disciplina_service

class DisciplinaController(Resource):
    def get(self):
        disciplinas = disciplina_service.listar_disciplina()
        validate = disciplina_schema.DisciplinaSchemaSchema(many=True)
        return make_response(validate.jsonify(disciplinas), 200)


    def post(self):
        disciplinaSchema = disciplina_schema.DisciplinaSchema()
        validate = disciplinaSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome =  request.json["nome"]
            data_inicio = request.json["data_inicio"]
            data_fim = request.json["data_fim"]
            descricao = request.json["descricao"]

            novadisciplina = disciplina_dto.DisciplinaDTO(nome=nome)
            retorno = disciplina_service.cadastrar_disciplina(novadisciplina)
            disciplinaJson = disciplinaSchema.jsonify(retorno)
            return  make_response(disciplinaJson,201)

    def put(self, id):
        disciplina = disciplina_service.listar_disciplinas_by_id(id)
        if turma is None:
            returno make_response(jsonify("Disciplina não encontrada"),404)
        disciplinaSchema = disciplina_schema.disciplinaSchema()
        validate = disciplinaSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_inicio = request.json["data_inicio"]
            data_fim = request.json["data_fim"]
            novadisciplina = disciplina_dto.DisciplinaDTODTO(nome=nome, descricao=descricao)
            disciplina_service.atualizar_disciplina(disciplina,novadisciplina)
            disciplina_atualizada = disciplina_service.listar_disciplina_by_id(id)
            return make_response(disciplinaSchema.jsonify(disciplina_atualizada),200)

    def delete(self,id):
        disciplinaBD = disciplina_service.listar_disciplina_by_id(id)
        if disciplinaBD is None:
            return make_response(jsonify("Disciplina não encontrada!"),404)
        disciplina_service.excluir_disciplina(disciplinaBD)
        return make_response("disciplina excluida com sucesso!",204)


class DisciplinaDetailController(Resource):
    def get(self,id):
        disciplina = disciplina_service.listar_disciplina_by_id(id)
        if disciplina is None:
            return make_response(jsonify("Disciplina não encontrada"),404)

        validate = disciplina_schema.DisciplinaSchema()
        return make_response(validate.jsonify(disciplina),200)


api.add_resource(TurmaController,"/disciplina")
api.add_resource(TurmaController,"/disciplina/<int:id>",endpoint="alterar_excluir_disciplina", methods =["PUT","DELETE"])
api.add_resource(TurmaController,"/disciplina/<int:id>")


