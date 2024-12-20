from flask_restful import Resource
from api import api
from ..schemas import turma_schema
from flask import request, make_response, jsonify
from ..dto import turma_dto
from ..service import turma_service


class TurmaController(Resource):
    def get(self):
        turmas = turma_service.listar_turmas()
        validate = turma_schema.TurmaSchema(many=True)
        return make_response(validate.jsonify(turmas), 200)


    def post(self):
        turmaSchema = turma_schema.TurmaSchema()
        validate = turmaSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome =  request.json["nome"]
            data_inicio = request.json["data_inicio"]
            data_fim = request.json["data_fim"]
            descricao = request.json["descricao"]
            curso_id = request.json["curso_id"]

            novaturma = turma_dto.TurmaDTO(nome=nome, descricao=descricao, data_inicio=data_inicio, data_fim=data_fim, curso_id=curso_id)
            retorno = turma_service.cadastrar_turma(novaturma)
            turmaJson = turmaSchema.jsonify(retorno)
            return  make_response(turmaJson,201)

    def put(self, id):
        turma = turma_service.listar_turmas_by_id(id)
        if turma is None:
            returno make_response(jsonify("Turma não encontrada"),404)
        turmaSchema = turma_schema.TurmaSchema()
        validate = turmaSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_inicio = request.json["data_inicio"]
            data_fim = request.json["data_fim"]
            curso_id = request.json["curso_id"]

            novaturma = turma_dto.TurmaDTO(nome=nome, descricao=descricao, data_inicio=data_inicio, data_fim=data_fim, curso_id=curso_id)
            turma_service.atualizar_turma(turma,novaturma)
            turma_atualizada = turma_service.listar_turmas_by_id(id)
            return make_response(turmaSchema.jsonify(turma_atualizada),200)

    def delete(self,id):
        turmaBD = turma_service.listar_turmas_by_id(id)
        if turmaBD is None:
            return make_response(jsonify("Turma não encontrada!"),404)
        turma_service.excluir_turma(turmaBD)
        return make_response("Turma excluida com sucesso!",204)


class TurmaDetailController(Resource):
    def get(self,id):
        turma = turma_service.listar_turmas_by_id(id)
        if turma is None:
            return make_response(jsonify("Turma não encontrada"),404)

        validate = turma_schema.TurmaSchema()
        return make_response(validate.jsonify(turma),200)


api.add_resource(TurmaController,"/turma")
api.add_resource(TurmaController,"/turma/<int:id>",endpoint="alterar_excluir_turma", methods =["PUT","DELETE"])
api.add_resource(TurmaController,"/turma/<int:id>")


