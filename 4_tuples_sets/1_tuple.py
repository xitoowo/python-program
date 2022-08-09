# Кортежи
# Кортежи (tuple) — это также упорядоченные наборы элементов.
# От списков их отличает одно: кортежи неизменяемы.
# То есть, после объявления кортежа изменить его элементы мы не сможем.
# Кортежи намного быстрее списков. Для получения доступа к элементам кортежа мы можем использовать индексы и срезы.

# Объявление пустого кортежа
mytuple = ()
mytuple = tuple()
print(mytuple)  # ()

# Кортеж интов
mytuple = (1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
print(mytuple)

# Кортеж с различными типами данных
mytuple = (1, 'Hello', 3.5)  # (1, 'Hello', 3.5)
print(mytuple)

# При создании кортежа необязательно использовать скобки
mytuple = 1, 'Hello', 3.5  # (1, 'Hello', 3.5)
print(mytuple)

# Особенность создания котежа с одним элементом!
mytuple = ('hello')
print(type(mytuple))  # <class 'str'>
mytuple = ('hello',)
print(type(mytuple))  # <class 'tuple'>
# Без скобок
mytuple = 'hello'
print(type(mytuple))  # <class 'str'>
mytuple = 'hello',
print(type(mytuple))  # <class 'tuple'>

# Вложенный кортеж
mytuple = (1, 2, (3, 4), 5)  # (1, 2, (3, 4), 5)
print(mytuple)

# Распаковка кортежа
mytuple = 3, 4.6, 'world'
a, b, c = mytuple
print(a, b, c)  # 3 4.6 world

# "Запаковка" кортежа
a = 'a'
b = 'b'
c = 'c'
mytuple = a, b, c
print(mytuple)

# Индексация и обращение к элементам
mytuple = ('h', 'e', 'l', 'l', 'o')
print(mytuple[0])  # h
print(mytuple[2])  # l
print(mytuple[-1])  # o
# print(mytuple[1.5])  # TypeError: tuple indices must be integers or slices, not float
# print(mytuple[99])  # IndexError: tuple index out of range
# print(mytuple[-1])  # IndexError: tuple index out of range

# Индексация и обращение к элементам вложенного списка
mytuple = ('World', (1, 2, 3), 4, [5.6, 7.8], ('H'), 'ello')
print(mytuple[0])  # World
print(mytuple[0][1])  # o
print(mytuple[1][1])  # 2
print(mytuple[-3][0])  # 5.6

# Элементы указанные без запятой, будут считаться одним элементом
mytuple = ('H', 'e' 'l' 'l' 'o' 'W', 'o', 'r' 'l' 'd', '!')
print(mytuple)  # ('H', 'elloW', 'o', 'rld', '!')

print('-'*80)
# Срезы кортежей
mytuple = ('H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!')
print(mytuple)  # ('H', 'e', 'l', 'l', 'W', 'o', 'r', 'l', 'd', '!')
print(mytuple[2:5])  # ('l', 'l', 'o')
# От начала до 5 индекса
print(mytuple[:5])  # ('H', 'e', 'l', 'l', 'o')
# С 2 индекса до конца
print(mytuple[2:])  # ('l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!')
# Полный срез (Копирование кортежа, поведение как у списков)
print(mytuple[:])  # ('H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!')
# Отрицательный срез
print(mytuple[-5:-2])  # ('o', 'r', 'l')
# Отрицательный срез до начала до -5 индекса
print(mytuple[:-5])  # ('H', 'e', 'l', 'l', 'o', 'W')
# Отрицательный срез с -3 индекса до конца
print(mytuple[-3:])  # ('l', 'd', '!')

# Изменение значений
# Кортеж четных чисел
mytuple = (2, 4, 6, 8)
print(mytuple)  # [2, 4, 6, 8]
# Изменение значений в кортеже невозможна
# mytuple[0] = 1  # TypeError: 'tuple' object does not support item assignment

# Изменение значений списка в кортеже возможна
mytuple = (2, [4, 6], 8)
mytuple[1][0] = 1
print(mytuple)  # (2, [1, 6], 8)

# Склейка кортежей
mytuple = (1, 2, 3) + (4, 5, 6)
print(mytuple)  # (1, 2, 3, 4, 5, 6)

# Склеивать можно только одинаковые типы данных
# mytuple = (1, 2, 3) + [4, 5, 6]  # TypeError: can only concatenate tuple (not "list") to tuple

# Методы кортежей
mytuple = ('h', 'e', 'l', 'l', 'o')
print(mytuple.count('l'))  # 2
print(mytuple.index('e'))  # 1

# In
mytuple = ('h', 'e', 'l', 'l', 'o')
print('l' in mytuple)  # True
print('a' in mytuple)  # False

# Повторение
print(('Hello',) * 3)  # ('Hello', 'Hello', 'Hello')

# Удаление
mytuple = ('h', 'e', 'l', 'l', 'o')
print(sorted(mytuple))
# Удаление элемента в кортеже невозможна
# del mytuple[0]  # TypeError: 'tuple' object doesn't support item deletion

# Удаление кортежа
del mytuple
# print(mytuple)  # NameError: name 'mytuple' is not defined
