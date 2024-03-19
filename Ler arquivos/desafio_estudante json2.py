import json

with open("estudantes.json") as file:
    data = json.load(file)
    

with open("estudantes_above_7.json", "w") as file_above_7: \
    open("estudantes_below_7.json", "w") as file_below_7:
        
    students_above_7 = [for s in data['students'] if s["avg_grade"] >= 70]
    students_above_7 = [for s in data['students'] if s["avg_grade"] < 70] 
    
    json.dump({"students": students_above_7}, file_above_7)
    json.dump({"students": students_below_7}, file_below_7)