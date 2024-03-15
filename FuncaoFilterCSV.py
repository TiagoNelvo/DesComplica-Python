import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv.reader:
            data.append(row)
    return data

csv_file_path = 'produtos.csv'
data_list = read_csv_file(csv_file_path)
print(data_list)

filtered_data = list(filter( lambda x: x[2].stip() == 'eletrodoméstico' , data_list))

print(filtered_data)