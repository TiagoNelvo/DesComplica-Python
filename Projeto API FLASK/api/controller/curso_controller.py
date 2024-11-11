from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..dto import curso_dto
from ..service import curso_service


class cursoController(Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        validate = curso_schema.CursoSchema(many=True)
        return make_response(validate.jsonify(cursos), 200)


    def post(self):
        cursoSchema = curso_schema.CursoSchema()
        validate = cursoSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome =  request.json["nome"]
            data_inicio = request.json["data_inicio"]
            data_fim = request.json["data_fim"]
            descricao = request.json["descricao"]
            disciplinas = request.json["disciplinas"]

            novacurso = curso_dto.cursoDTO(nome=nome, descricao=descricao, data_inicio=data_inicio, data_fim=data_fim)
            retorno = curso_service.cadastrar_curso(novacurso)
            cursoJson = cursoSchema.jsonify(retorno)
            return  make_response(cursoJson,201)

    def put(self, id):
        curso = curso_service.listar_cursos_by_id(id)
        if curso is None:
            returno make_response(jsonify("curso não encontrada"),404)
        cursoSchema = curso_schema.CursoSchema()
        validate = cursoSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_inicio = request.json["data_inicio"]
            data_fim = request.json["data_fim"]
            novacurso = curso_dto.CursoDTO(nome=nome, descricao=descricao, data_inicio=data_inicio, data_fim=data_fim, disciplinas=disciplinas)
            curso_service.atualizar_curso(curso,novacurso)
            curso_atualizada = curso_service.listar_cursos_by_id(id)
            return make_response(cursoSchema.jsonify(curso_atualizada),200)

    def delete(self,id):
        cursoBD = curso_service.listar_cursos_by_id(id)
        if cursoBD is None:
            return make_response(jsonify("curso não encontrada!"),404)
        curso_service.excluir_curso(cursoBD)
        return make_response("curso excluida com sucesso!",204)


class cursoDetailController(Resource):
    def get(self,id):
        curso = curso_service.listar_cursos_by_id(id)
        if curso is None:
            return make_response(jsonify("curso não encontrada"),404)

        validate = curso_schema.cursoSchema()
        return make_response(validate.jsonify(curso),200)


api.add_resource(cursoController,"/curso")
api.add_resource(cursoController,"/curso/<int:id>",endpoint="alterar_excluir_curso", methods =["PUT","DELETE"])
api.add_resource(cursoDetailController,"/curso/<int:id>")


