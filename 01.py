## Calculo base Custo final = Custo de fábrica + (Custo de fábrica * 0.28) + (Custo de fábrica * 0.45)

Custo_Fabrica = int(input('Digite o Custo de Fábrica da produção do carro:'))
# calculo
Custo_Final = Custo_Fabrica + (Custo_Fabrica * 0.28) + (Custo_Fabrica * 0.45)
print('O Custo Final do carro é de: ', Custo_Final)

## Outra Maneira
Custo_Fabrica = int(input('Digite o Custo de Fábrica da produção do carro:'))

## Calculo
distribuidor = Custo_Fabrica * 0.28
imposto = Custo_Fabrica * 0.45
##

CF = Custo_Fabrica + distribuidor + imposto
print('O Custo Final do carro é de: ', CF)