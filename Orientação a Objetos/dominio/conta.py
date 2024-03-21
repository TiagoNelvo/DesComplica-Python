class Conta:
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        
    def resumo(self):
        print(f"Conta Corrente: {self.numero} saldo: {self.saldo}")
        
        
    def deposito(self,valor):
        self.saldo += valor
        
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor   