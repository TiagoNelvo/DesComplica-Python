class MinhaException(Exception):
    pass

def calculo(num):
    if num < 2:
        raise MinhaException("O número não pode ser menor que 2")
    print("Numero informado com sucesso")

try:
    calculo(1)
except MinhaException:
    print("Minha Exception foi chamada")