import csv
import json

DATA1 = []
with open('json_to_csv.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        DATA1.append(line)

with open('csv_to_json.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA1, file, ensure_ascii=False, indent=4)

DATA2 = []
with open('json_to_csv1.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        DATA2.append(line)

with open('csv_to_json1.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA2, file, ensure_ascii=False, indent=4)

DATA3 = []
with open('json_to_csv2.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        DATA3.append(line)

with open('csv_to_json2.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA3, file, ensure_ascii=False, indent=4)

DATA4 = []
with open('json_to_csv3.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        DATA4.append(line)

with open('csv_to_json3.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA4, file, ensure_ascii=False, indent=4)

DATA5 = []
with open('json_to_csv4.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        DATA5.append(line)

with open('csv_to_json4.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA5, file, ensure_ascii=False, indent=4)

DATA6 = []
with open('json_to_csv5.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        DATA6.append(line)

with open('csv_to_json5.json', mode='w', encoding='UTF-8') as file:
    json.dump(DATA6, file, ensure_ascii=False, indent=4)
