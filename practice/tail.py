import os.path


class EmptyPath(Exception):
    pass


class FileNotExists(Exception):
    pass


file_name = input('Введите название файла: ')
if not file_name:
    raise EmptyPath('Пустой ввод')

if not os.path.exists(file_name):
    raise FileNotExists(f'Такого файла не существует: {file_name}')

with open(file_name, 'r', encoding='utf-8') as source:
    strings = []
    for line in source:
        strings.append(line)
        if len(strings) > 10:
            strings.pop(0)


for l in strings:
    print(l, end='')
