class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def setNome(self, nome):
        self.nome = nome
        
    def getNome(self):
        return self.nome
    
    def setIdade(self,idade):
        self.idade = idade
        
    def getIdade(self):
        return self.idade
    
pessoaMarcelo = Pessoa("Marcelo", 33)
pessoaMarcelo.setNome("Marcelo Silva")
pessoaMarcelo.setIdade("40")
print(pessoaMarcelo.getNome())
print(pessoaMarcelo.getIdade())

pessoaLucas = Pessoa("Lucas",26)
pessoaLucas.setNome("Lucas Guilherme")
print(pessoaLucas.getNome())
