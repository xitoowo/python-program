# Встроенные функции Python
# Интерпретатор Python имеет ряд функций, которые всегда доступны для использования. Эти функции называются встроенными.
#
# Например, функция print() выводит указанный объект на устройство вывода (экран) или в файл текстового потока.

# enumerate
# Метод enumerate() добавляет счетчик к итерируемому объекту и возвращает индексы элементов с их значениями.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
for index, i in enumerate(nums, start=1):  # По умолчанию start = 0
    print(index, i)

print()
# zip
# Функция zip() объединяет в кортежи элементы из последовательностей
# позволяет пройтись одновременно по нескольким итерируемым объектам (спискам и др.)
# Различие между zip и itertools.product в том, что zip создает интератор, а product возвращает генератор
a = [1, 2, 3]
b = 'xyz'
c = ('None', True, None)

for x in zip(a, b, c):
    print(type(x), x)  # <class 'tuple'> (1, 'x', 'None') ...
print()

for x, y, z in zip(a, b, c):
    print(x, y, z)  # 1 x None ...
print()

result = list(zip(a, b, c))
print(result)  # [(1, 'x', 'None'), (2, 'y', True), (3, 'z', None)]

print()
# reduce применяет переданную функцию к итерируемому объекту и возвращает одно значение.
from functools import reduce

print(reduce(lambda a, b: a + b, [23, 21, 45, 98]))  # 187

print()


# filter используется для создания списка, состоящего из значений, для которых функция возвращает true.
def func(x):
    if x >= 3:
        return x


y = filter(func, (1, 2, 3, 4))
print(y)  # <filter object at 0x000002A3DF772F70>
print(list(y))  # [3, 4]

print()


# map функция принимает другую функцию в качестве параметра вместе с итерируемой последовательностью и
# возвращает выходные данные после применения функции на каждый итерируемый элемент из последовательности.
def func(a, b):
    return a + b


a = map(func, [2, 4, 5], [1, 2, 3])
print(a)  # <map object at 0x00000222719C4F10>
print(list(a))  # [3, 6, 8]

# Факториал с помощью reduce
#
nums = [1, 2, 3, 4, 5]


def add_my(a, b):
    return a * b


result = reduce(add_my, nums)
print(result)


def square(number):
    return number ** 2


nums = [2, 4, 6, 8]
result = list(map(square, nums))
print(result)

abs_values = list(map(abs, [-1, -2, -3, 0]))
print(abs_values)
input_data = '1 2 3 4 5 6'.split(' ')
floated = list(map(int, input_data))
print(floated)
words = ['hello', 'world', 'hi', 'peace']
result = list(map(len, words))
print(result)
