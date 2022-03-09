# Функции
# Простая функция без параметров
def hello_world():
    """
    docstring - описание функции
    """
    print('Hello, World!')


# Функцию необходимо вызвать
hello_world()  # Hello, World!
print(hello_world.__doc__)  # docstring - описание функции


# Функция с параметрами
def greet(name):
    print(f'Hello, {name}!')


greet('John')  # Hello, John!

# Вызов функции при итерации по списку
names = ['Joe', 'Bob', 'Elsa']
for name in names:
    greet(name)

# Hello, John!
# Hello, Joe!
# Hello, Bob!
# Hello, Elsa!
