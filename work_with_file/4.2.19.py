import csv
from datetime import datetime


with open('name_log.csv', 'r', encoding='utf-8') as file:
    datas = list(csv.reader(file))
    colm = datas[0]
    datas = datas[1:]
    datas = list(map(lambda row: [row[0], row[1], datetime.strptime(row[2], '%d/%m/%Y %H:%M')], datas))
    dct = {email: [] for email in {row[1] for row in datas}}
    spisok = {}
    for data in datas:
        spisok[data[1]] = spisok.get(data[1], data)
        if spisok[data[1]][2] < data[2]:
            spisok[data[1]] = data
    email = sorted(spisok)

for key, value in spisok.items():
    spisok[key] = [value[0], value[1], datetime.strftime(value[2], '%d/%m/%Y %H:%M')]

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(colm)
    for key in email:
        writer.writerow(spisok[key])