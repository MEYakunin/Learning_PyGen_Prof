from datetime import datetime


def get_messeges():
    messages = []
    mess = ''
    with open('diary.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if line == '\n':
                messages.append(mess.split('\n'))
                mess = ''
                continue
            else:
                mess += line
    return messages


def sort_messages():
    data = sorted(get_messeges(), key=lambda mess: datetime.strptime(mess[0], '%d.%m.%Y; %H:%M'))
    del data[-1][-1]
    return data

data = sort_messages()
for i in range(1, len(data)):
    data[i][0] = '\n' + data[i][0]

with open('clue.txt', 'w', encoding='utf-8') as file:
    for message in data:
        print(*message, sep='\n', end='', file=file)




