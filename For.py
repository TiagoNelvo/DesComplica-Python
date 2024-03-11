for numero in range(6):
    print(numero)
print('******')

for numero1 in range(1,5):
    print(numero1)
    print('___')
print('******')

for numero2 in range(1,20,2):
    print(numero2)
    print('___')
print('******')

flagcompra = False
info = "Compra efetuada"

for tentativa in range(3):
    if flagcompra:
        print(info)
        break
else:
    print("Houve um problema na compra")
print('******')

lista = [1,2,3,4,5]
for item in lista:
    print(item) 
    print('---') 
print('******')  

frutas1 = ["abacate", "banana", "morango"]
frutas2 = []
for fruta in frutas1:
    if 'n' in fruta:
        frutas2.append(fruta)
print(frutas2)

frutas3 = [fruta for fruta in frutas1 if 'n' in fruta]
print(frutas3)

print('******')

index = 0
for fruta in frutas1:
    print(index,fruta)
    index += 1
    
for cont, fruta in enumerate(frutas1):
    print(cont, fruta)
print('******')