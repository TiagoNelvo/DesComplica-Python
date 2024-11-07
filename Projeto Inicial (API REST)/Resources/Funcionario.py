from flask_restful import Resource , reqparse

funcionarios = [{"id_funcionario":1, "nome":'Lucas','email':'lucas@gmail.com'},
                {"id_funcionario":2, "nome":'Joao','email':'joao@gmail.com'}
                ]

class Funcionario(Resource):
    
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('id_funcionario')
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    
    def get(self):
        return funcionarios
    
    def post(self):        
              
        dados = Funcionario.argumentos.parse_args()
        
        novo_funcionario = {
            "id_funcionario": dados['id_funcionario'],
            "nome": dados['nome'],
            "email": dados['email']
        }
        
        
        funcionarios.append(novo_funcionario)
        return novo_funcionario, 200

    def getFuncionarioId(id):
        for funcionario in funcionarios:
            if funcionario['id_funcionario'] == id:
                return funcionario
            return None
    
    def put(self,id):
        dados = Funcionario.argumentos.parse_args()
        
        
        novo_funcionario = {
            "id_funcionario": id, **dados
        }
        funcionario = Funcionario.getFuncionarioId(id)
        if funcionario:
            funcionario.update(novo_funcionario)
            return novo_funcionario, 200
        funcionarios.append(novo_funcionario)
        return novo_funcionario, 201
        
    def delete(self,id):
        global funcionarios
        funcionarios = [func for func in funcionarios if func['id_funcionario'] != id]
        return { "message": "Funcionario excluido"}
        
        
        