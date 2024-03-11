import logging

logging.basicConfig(filename="logApp.log", level= logging.DEBUG)

def calculoValores(num1,num2):
    try:
        resultado = num1/num2
    except ZeroDivisionError:
        logging.exception("Problema na divisão do numero por zero")
    else:
        return resultado    
    
print(calculoValores(2,0))