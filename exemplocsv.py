import csv

with open('produtos.csv', encoding="utf-8") as file:
    ler_csv = csv.reader(file)
    for row in ler_csv:
        print(row)    
