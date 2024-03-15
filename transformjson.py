import json

dado = {
    "nome": "Lucas",
    "idade": 30,
    "cidade": "Rio de Janeiro"
}

with open("data.json", "w") as file:
    json.dump(dado,file)
    
with open("data.json", "r") as f:
    data = json.load(f)

print(data)