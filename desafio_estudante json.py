import json

with open("estudantes.json") as file:
    data = json.load(file)
    
for student in data['students']:
    grades = student["grades"]
    avg_grade =  sum(grades) / len (grades)
    student["avg_grade"] = avg_grade
    
with open("estudandes.json", "w") as file:
    json.dump(data,file,indent=2)
    
print(json.dump(data, indent=2))