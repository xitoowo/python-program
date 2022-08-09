# Словари
# Это коллекция, в которой данные хранятся в виде пар ключ-значение {key:value}
# Словари упорядочены и изменяемы, а данные в них не могут дублироваться.
# При этом стоит иметь в виду, что до Python 3.6 словари были не упорядочены.

# Создание словаря
mydict = {}
mydict = dict()
print(mydict)  # {}

# Ключ: значение
mydict = {'name': 'Bob', 'job': 'dev', 'age': '40'}
print(mydict)  # {'name': 'Bob', 'job': 'dev', 'age': '40'}
# Ключами могут быть только неизменяемые типы данных
mydict = {1: 'Bob', 2: 'dev', 3: '40'}
print(mydict)  # {1: 'Bob', 2: 'dev', 3: '40'}
mydict = {(1, 2): 'Bob', (3, 4): 'dev', (5, 6): '40'}
print(mydict)  # {(1, 2): 'Bob', (3, 4): 'dev', (5, 6): '40'}
# mydict = {[1, 2]: 'Bob', (3, 4): 'dev', (5, 6): '40'}  # TypeError: unhashable type: 'list'

# Создание ключа по ключевым словам, ключ указывается без ковычек
mydict = dict(name='Bob', job='dev', age=40)
print(mydict)  # {'name': 'Bob', 'job': 'dev', 'age': 40}

# Создание словаря из последовательности
# dict([(ключ, значение), ...])
mydict = dict([(1, 'Bob'), (2, 'dev'), (3, '40')])
print(mydict)  # {1: 'Bob', 2: 'dev', 3: '40'}

# Словарь со списком
mydict = {'name': 'Bob', 'job': ['dev', 'manager', 'boss'], 'age': '40'}
print(mydict)  # {'name': 'Bob', 'job': ['dev', 'manager', 'boss'], 'age': '40'}

# Вложенный словарь
mydict = {'names': {'Bob': 'dev', 'Jane': 'manager', 'Joe': 'boss'}, 'age': '40'}
print(mydict)  # {'names': {'Bob': 'dev', 'Jane': 'manager', 'Joe': 'boss'}, 'age': '40'}

# Доступ к элементам
mydict = {'name': 'Bob', 'job': 'dev', 'age': '40'}
print(mydict['name'])  # Bob
# При доступе к несуществующему ключу, будет ошибка KeyError
# print(mydict['abcb'])  # KeyError: 'abcb'
# У словарей существует метод get(), который возвращает значение по умолчанию, если ключа нет
print(mydict.get('job'))  # dev
print(mydict.get('age', 'default'))  # 40
# Возврат значения по умолчанию
print(mydict.get('abcd'))  # None
print(mydict.get('abcd', 'default'))  # default

# Изменение значений
mydict = {'name': 'Bob', 'job': 'manager'}
print(mydict)  # {'name': 'Bob', 'job': 'manager'}
mydict['name'] = 'Jane'
print(mydict)  # {'name': 'Jane', 'job': 'manager'}
# Изменение значений у несуществующего ключа приведет к его созданию
mydict['age'] = 45
print(mydict)  # {'name': 'Jane', 'job': 'manager', 'age': 45}

# Методы словарей
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Обновление словаря методом update({ключ: значение})
# Дополняем
squares.update({6: 36})  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print(squares)
# Обновляем
squares.update({6: 0})  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 0}
print(squares)

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Вывод ключей и значений с формате списка с кортежами (ключ: значение)
print(squares.items())  # dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
# Вывод только ключей
print(squares.keys())  # dict_keys([1, 2, 3, 4, 5])
# Вывод только значений
print(squares.values())  # dict_values([1, 4, 9, 16, 25])

# Удаление значений
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Удаление методом pop с возвратом значения
# Если ключ не найден, возвращает значение по умолчанию.
print(squares.pop(4))  # 16
print(squares)  # {1: 1, 2: 4, 3: 9, 5: 25}
# print(squares.pop(6))  # KeyError: 6
print(squares.pop(6, 36))  # 36

# Удаление методом popitem произвольного элемента с возвратом значения
print(squares.popitem())  # (5, 25)
print(squares)  # {1: 1, 2: 4, 3: 9}

# Очистка словаря
squares.clear()
print(squares)  # {}

