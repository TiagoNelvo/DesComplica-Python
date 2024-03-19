from pessoa import Pessoa


class PessoaFisica(pessoa):
    
    def __init__(self, CPF, nome, idade):
        super().__init__(nome,idade)
        self.cpf = CPF
        
def getCPF(self):
    return self.cpf

def setCPF(self, CPF):
    self.cpf = CPF
    
    
pessoaFisica = PessoaFisica("22244455599", "Marcelo", 33)
print(pessoaFisica.getNome())
print(pessoaFisica.getIdade())
print(pessoaFisica.getCPF())