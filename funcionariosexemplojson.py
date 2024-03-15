import json

with open('empregados.json', encoding='utf-8') as f:
    dados = json.load(f)
    

for dado in dados['funcionarios']:
    if dado['nome'] == 'Lucas': 
        dado['endereco']['rua'] = 'Rua das Flores 40'
        #print(dado['endereco']['rua'])
        
with open('empregados_modificado.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)
        
print(dados['funcionarios'][1]['endereco']['rua'])        