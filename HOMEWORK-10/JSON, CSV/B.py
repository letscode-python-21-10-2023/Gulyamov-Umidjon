import csv
import json

with open('posts.json', encoding='UTF-8') as file:
    DATA1 = json.load(file)


with open('json_to_csv5.csv', 'w', encoding='cp1251', newline='') as file:
    DictWriter = csv.DictWriter(file, fieldnames=['Айди пользователя', 'Айди', 'Заголовок', 'Тело'])
    DictWriter.writeheader()
    for line in DATA1:
        DictWriter.writerow(line)


import csv
import json

with open('comments.json', encoding='UTF-8') as file:
    DATA2 = json.load(file)


with open('json_to_csv4.csv', 'w', encoding='cp1251', newline='') as file:
    DictWriter = csv.DictWriter(file, fieldnames=['Айди поста', 'Айди', 'Имя', 'Почта', 'Тело'])
    DictWriter.writeheader()
    for line in DATA2:
        DictWriter.writerow(line)


import csv
import json

with open('albums.json', encoding='UTF-8') as file:
    DATA3 = json.load(file)


with open('json_to_csv3 .csv', 'w', encoding='cp1251', newline='') as file:
    DictWriter = csv.DictWriter(file, fieldnames=['Айди пользователя', 'Айди', 'Заголовок'])
    DictWriter.writeheader()
    for line in DATA3:
        DictWriter.writerow(line)


import csv
import json

with open('photos.json', encoding='UTF-8') as file:
    DATA4 = json.load(file)


with open('json_to_csv2.csv', 'w', encoding='cp1251', newline='') as file:
    DictWriter = csv.DictWriter(file, fieldnames=['Айди альбома', 'Айди', 'Заголовок', 'URL', 'URL миниатюры'])
    DictWriter.writeheader()
    for line in DATA4:
        DictWriter.writerow(line)


import csv
import json

with open('todos.json', encoding='UTF-8') as file:
    DATA5 = json.load(file)


with open('json_to_csv1.csv', 'w', encoding='cp1251', newline='') as file:
    DictWriter = csv.DictWriter(file, fieldnames=['Айди пользователя', 'Айди', 'Заголовок', 'Завершение'])
    DictWriter.writeheader()
    for line in DATA5:
        DictWriter.writerow(line)

import csv
import json

with open('users.json', encoding='UTF-8') as file:
    DATA = json.load(file)


with open('json_to_csv.csv', 'w', encoding='cp1251', newline='') as file:
    DictWriter = csv.DictWriter(file, fieldnames=['Имя', 'Логин', 'Почта', 'Номер', 'Адрес'])
    DictWriter.writeheader()
    for line in DATA:
        DictWriter.writerow(line)
