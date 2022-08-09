# Форматирование строк
# Существует несколько способов форматирования строк

print('% / Python 2')
# Старый способ / Python 2
# Раньше форматирование строк происходило при помощи оператора %
hello = "Hi, my name is %s" % "Jane"
# Вывод: Hi, my name is Jane
print(hello)

hello = "Hi, my name is %s %s" % ("Jane", "Doe")
# Вывод: Hi, my name is Jane Doe
print(hello)

print('Format')
# Использование метода format
# Подстановка по порядку
names = "{}, {} and {}".format("John", "Bob", "Jane")
# Вывод: John, Bob and Jane
print(names)

# Подстановка по позиционному (positional) аргументу
names = "{2}, {0} and {1}".format("John", "Bob", "Jane")
# Вывод: Jane, John and Bob
print(names)

# Подстановка по аргументу ключевому (keyword) слову
names = "{a}, {c} and {b}".format(a="John", b="Bob", c="Jane")
# Вывод: John, Jane and Bob
print(names)

print('f-строки')
# Использование f-строк
names = f"{'John'}, {'Bob'} and {'Jane'}"
# Вывод: John, Bob and Jane
print(names)

john = 'John'
bob = 'Bob'
jane = 'Jane'
names = f'{jane}, {bob} and {john}'
# Вывод: Jane, Bob and John
print(names)

print('-' * 10)

# Примеры форматирования с format и f-строками
# Вывод числа в разных форматах
# Вывод: int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
# Вывод: int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010
print(f"int: {42:d};  hex: {42:#x};  oct: {42:#o};  bin: {42:#b}")

# Выравнивание строк
# Вывод: Cat
print("{:15}".format('Cat'))  # Лево
# Вывод:             Cat
print("{:>15}".format('Cat'))  # Право
# Вывод:       Cat
print("{:^15}".format('Cat'))  # Центр
# Вывод: ******Cat******
print("{:*^15}".format('Cat'))  # Центр с заполнением символа *

# Вывод: Cat
print(f"{'Cat':15}")
# Вывод:             Cat
print(f"{'Cat':>15}")
# Вывод:       Cat
print(f"{'Cat':^15}")
# Вывод: ******Cat******
print(f"{'Cat':*^15}")

# Выравнивание чисел
# Целочисленные
# Вывод:    12
print("{:5d}".format(12))  # Отступ с шириной
# Вывод: 12345
print("{:2d}".format(12345))  # Отступ не работает, если число больше ширины
# Дробные
# Вывод: 012.2457
print("{:08.4f}".format(12.2456845))  # Отступ заполненный нулями и ограничение тремя знаками после запятой
# Вывод: 12.246
print("{:2.3f}".format(12.2456845))  # Отступ заполненный нулями и ограничение тремя знаками после запятой
