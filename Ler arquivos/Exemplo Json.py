import json

with open('dados.json', encoding="utf-8") as file:
    dados = json.load(file)
    
for dado in dados:
    print(dado['nome'], dado['idade'])