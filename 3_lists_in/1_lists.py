# Списки
# Список в Python представлят из себя последовательность элементов с возможностью хранить различные типы данных
# в отличии от массивов
# Реализация схожа с  динамическим массивом

# Объявление пустого списка списка
mylist = []
mylist = list()
print(mylist)  # []
# Список интов
mylist = [1, 2, 3, 4, 5]  # [1, 2, 3, 4, 5]
print(mylist)
# Список с различными типами данных
mylist = [1, 'Hello', 3.5]  # [1, 'Hello', 3.5]
print(mylist)

# Вложенный список
mylist = ['World', [1, 2, 3], 4, [5.6, 7.8], ['H'], 'ello']
print(mylist)  # ['World', [1, 2, 3], 4, [5.6, 7.8], ['H'], 'ello']

# Индексация и обращение к элементам
# В [] необходимо указать индекс элемента в формате целого числа
# При указании индекса большего, чем длина списка будет ошибка выход за пределы списка
# Индексация начинается с 0
#          0    1    2    3    4
mylist = ['h', 'e', 'l', 'l', 'o']
print(mylist[0])  # h
print(mylist[2])  # l
print(mylist[-1])  # o
# print(mylist[1.5])  # TypeError: list indices must be integers or slices, not float
# print(mylist[99])  # IndexError: list index out of range
# print(mylist[-1])  # IndexError: list index out of range

# Индексация и обращение к элементам вложенного списка
mylist = ['World', [1, 2, 3], 4, [5.6, 7.8], ['H'], 'ello']
print(mylist[0])  # World
print(mylist[0][1])  # o
print(mylist[1][1])  # 2
print(mylist[-3][0])  # 5.6

# Элементы указанные без запятой, будут считаться одним элементом
mylist = ['H', 'e' 'l' 'l' 'o' 'W', 'o', 'r' 'l' 'd', '!']
print(mylist)  # ['H', 'elloW', 'o', 'rld', '!']

# Срезы списков
mylist = ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']
print(mylist)  # ['H', 'e', 'l', 'l', 'W', 'o', 'r', 'l', 'd', '!']
print(mylist[2:5])  # ['l', 'l', 'o']
# От начала до 5 индекса
print(mylist[:5])  # ['H', 'e', 'l', 'l', 'o']
# С 2 индекса до конца
print(mylist[2:])  # ['l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']
# Полный срез (Копирование списка, об этом в 1_list_advanced)
print(mylist[:])  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']
# Отрицательный срез
print(mylist[-5:-2])  # ['o', 'r', 'l']
# Отрицательный срез до начала до -5 индекса
print(mylist[:-5])  # ['H', 'e', 'l', 'l', 'o', 'W']
# Отрицательный срез с -3 индекса до конца
print(mylist[-3:])  # ['l', 'd', '!']

# Изменение значений
# Список четных чисел
mylist = [2, 4, 6, 8]
print(mylist)  # [2, 4, 6, 8]
# Изменение одного элемента по индексу 0
mylist[0] = 1
print(mylist)  # [1, 4, 6, 8]
# Вставка нескольких значений
mylist = [2, 4, 6, 8]
print(mylist)  # [2, 4, 6, 8]
mylist[0] = [1, 3, 5]
print(mylist)  # [[1, 3, 5], 4, 6, 8]
# Для вставки нескольких значений на 0 индекс нужно использовать срезы
mylist = [2, 4, 6, 8]
mylist[0:0] = [1, 3, 5]  # Изменение значений с 0-0 индекс, значения не перетираются
print(mylist)  # [1, 3, 5, 2, 4, 6, 8]

# Ошибка, нужно передавать только последовательность, например [1, 2, 3]
# mylist[2:2] = 1  # TypeError: can only assign an iterable

# Изменение значений с 1-4 индекс, значения перетираются
mylist = [2, 4, 6, 8]
mylist[1:4] = [1, 3, 5]
print(mylist)  # [2, 1, 3, 5]

# Склейка списков
mylist = [1, 2, 3] + [4, 5, 6]
print(mylist)  # [1, 2, 3, 4, 5, 6]

# Склеивать можно только одинаковые типы данных
# mylist = (1, 2, 3) + [4, 5, 6]  # TypeError: can only concatenate tuple (not "list") to tuple


# Методы списков
# Список нечетных чисел
mylist = [1, 3, 5]
print(mylist)  # [1, 3, 5]
# Метод append добавляет указанный элемент в конец списка
mylist.append(7)
print(mylist)  # [1, 3, 5, 7]
# Добавление нескольких значений используя append
mylist = [1, 3, 5]
print(mylist)  # [1, 3, 5]
# append добавляет элемент как он есть
mylist.append([7, 9, 11])
print(mylist)  # [1, 3, 5, [7, 9, 11]]

# Добавление нескольких значений
# Для добавления множества элементов необходимо использовать метод extend
mylist = [1, 3, 5]
print(mylist)  # [1, 3, 5]
mylist.extend([7, 9, 11])
# mylist.extend(7)  # extend ожидает на вход последовательность, поэтому передача одного элемента будет ошбикой
print(mylist)  # [1, 3, 5, 7, 9, 11]

# Вставка одного элемента на определенную позицию методом insert
# Элемент стоявший на указанной позиции, и все следующие смещаются вправо
mylist = [1, 2, 3, 4]
# insert(Индекс, элемент)
mylist.insert(3, 5)
print(mylist)  # [1, 2, 3, 5, 4]
mylist.insert(-1, 7)
print(mylist)  # [1, 2, 3, 5, 7, 4]

# Подсчет количества элементов в списке
mylist = [3, 9, 7, 1, 1, 3, 4, 5, 6, 6, 0]
# count(Значение)
print(mylist.count(0))  # 1
print(mylist.count(1))  # 2
print(mylist.count(6))  # 2

# Узнать индекс элемента
# Вернется индекс первого попавшегося элемента
mylist = [3, 9, 7, 1, 1, 3, 4, 5, 6, 6, 0]
# index(Значение)
print(mylist.index(0))  # 10
print(mylist.index(1))  # 3
print(mylist.index(6))  # 8

# Создание списка из строки
# sep - разделитель, по умлочанию пробел указывать его не нужно
mylist = 'H e l l o W o r l d !'.split()  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']
print(mylist)
mylist = 'H.e.l.l.o.W.o.r.l.d.!'.split(sep='.')  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']
print(mylist)
# maxsplit - максимальное количество разделений
mylist = 'H e l l o W o r l d !'.split(maxsplit=3)  # ['H', 'e', 'l', 'l o W o r l d !']
print(mylist)

# Удаление значений из списка методом remove (без возврата значения)
# remove(элемент) - удаляет первый попавшиеся элемент
mylist = 'H e l l o W o r l d !'.split()  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']
mylist.remove('l')
print(mylist)  # ['H', 'e', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']

# Задание - удалить все птовторяющиеся элементы

# Удаление значений из списка методом pop (возврата значения)
# pop(индекс) - удаляет элемент по индексу
mylist = 'H e l l o W o r l d !'.split()  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']
mylist.remove('l')
print(mylist)  # ['H', 'e', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']

mylist = 'H e l l o W o r l d !'.split()  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!']
mylist.pop()  # по умолчанию удаляет последний == mylist.pop(-1)
print(mylist)  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
mylist.pop(4)
print(mylist)  # ['H', 'e', 'l', 'l', 'W', 'o', 'r', 'l', 'd']
# Возврат значения означает, что можно перехватить удаленное значение
elem = mylist.pop(3)
print(mylist)  # ['H', 'e', 'l', 'W', 'o', 'r', 'l', 'd']
print(elem)  # l

# Очистка списка
mylist = 'H e l l o W o r l d !'.split()
mylist.clear()
print(mylist)  # []

# Повторение
print(['Hello'] * 3)  # ['Hello', 'Hello', 'Hello']
