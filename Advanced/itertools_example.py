import itertools
# Product
# Вложенные циклы — настоящая головная боль. Они усложняют не только сам код, но и его читаемость.
# Выход из этих циклов — задача тоже сложная.
# Чтобы найти ошибку, приходится приложить много усилий, ведь нужно проверить каждый внутренний цикл.
#
# К счастью, существует очень полезная встроенная функция — product.
# Она является частью встроенного модуля Python — itertools. С ее помощью мы можем избавиться от вложенных циклов.
#
# Схожа с zip, но без ограничений на количество аргументов
list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]
list_d = [1, 2020, 70]
list_e = [2, 4, 7, 2000]
list_j = [3, 70, 7]
# 1 2 3 1 2 3
# 1 2 3 1 2 70
# 1 2 3 1 2 7
# 1 2 3 1 4 3
# 1 2 3 1 4 70
# ...
# 70 2000 7 70 2000 3
# 70 2000 7 70 2000 70
# 70 2000 7 70 2000 7
for a, b, c, d, e, j in itertools.product(list_a, list_b, list_c, list_d, list_e, list_j):
    print(a, b, c, d, e, j)
qe = itertools.product(list_a, list_b, list_c, list_d, list_e, list_j)

# [(1, 2, 3, 1, 2, 3), (1, 2, 3, 1, 2, 70), (1, 2, 3, 1, 2, 7), (1, 2, 3, 1, 4, 3), (1, 2, 3, 1, 4, 70),
# ...
# (70, 2000, 7, 70, 2000, 70), (70, 2000, 7, 70, 2000, 7)]
print(list(qe))  # [(), (), ()]

# Создаем бесконечный цикл
# В модуле itertools есть как минимум три метода для создания бесконечных циклов:

# 1. Функция count.
natural_num = itertools.count(1)
for n in natural_num:
    print(n)  # 1,2,3,...

# 2. Функция cycle.
many_yang = itertools.cycle('Hello')
for y in many_yang:
    print(y)  # 'H','e','l','l','o','H','e','l',...

# 3. Функция repeat.
many_yang = itertools.repeat('Hello')
for y in many_yang:
    print(y)  # 'Hello','Hello',...


# Объединяем несколько итераторов в один
# Функция chain() помогает нам объединять несколько итераторов в один.
from itertools import chain
list_a = [1, 22]
list_b = [7, 20]
list_c = [3, 70]
for i in chain(list_a, list_b, list_c):
    print(i)  # 1,22,7,20,3,70

# Выводим повторяющиеся элементы и количество их повторений
# Функция groupby() позволяет получить повторяющиеся элементы в итераторе и сгруппировать их.
from itertools import groupby
for key, group in groupby('Pyttthhhonissst'):
    print(key, list(group))
# P ['P']
# y ['y']
# t ['t', 't', 't']
# h ['h', 'h', 'h']
# o ['o']
# n ['n']
# i ['i']
# s ['s', 's', 's']
# t ['t']

# Как видите, дублирующиеся буквы сгруппированы. Более того, мы можем расширить функционал groupby().
# Например, указать, что нужно игнорировать регистр:
from itertools import groupby
for key, group in groupby('PyYyYTTthHOoOnisst', lambda x: x.upper()):
    print(key, list(group))
# P ['P']
# Y ['y', 'Y', 'y', 'Y']
# T ['T', 'T', 't']
# H ['h', 'H']
# O ['O', 'o', 'O']
# N ['n']
# I ['i']
# S ['s', 's']
# T ['t']
