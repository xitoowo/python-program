# Функции
# Функция в Python – классический пример многократного использования кода.
# Функция – это подпрограмма, которая работает с данными и производит некоторый вывод.
#
# Чтобы определить функцию Python, вам нужно будет использовать ключевое слово def перед именем вашей функции.
# Сразу за именем добавляются круглые скобки, за которыми следует двоеточие.
#
# Python для обозначения блоков использует отступы вместо скобок, чтобы код был более читабельным.
#
# Функция в Python может содержать любое количество параметров или не содержать ни одного.
#
# Кроме того, функция может возвращать значение. Это может быть результат выполнения вашей функции или даже выражение
# или значение, указанное вами после ключевого слова return.
#
# После выполнения оператора return поток программы возвращается в состояние, следующее за вызовом вашей функции,
# и продолжает выполнение оттуда.
#
# Итак, функция в Python может вызываться в любом месте кода. Для вызова вам нужно будет использовать ее имя и
# при необходимости передать в нее аргументы в круглых скобках.
#
# Правила присвоения имени функции такие же, как для переменных. Имя должно начинаться или с буквы от A до Z в
# любом регистре, или с подчеркивания _. Остальная часть имени может содержать символы подчеркивания,
# цифры от 0 до 9, любые буквы в верхнем или нижнем регистре.
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

print()


# Цикл внутри функции
# * или астериск означает распакову последовательности и передачу элементов внутрь функции
def greet(*names):
    for name in names:
        print(f'Hello, {name}')


greet("John", "Carl", "Tom")
names = ['Joe', 'Bob', 'Elsa']
greet(*names)

# Hello, John
# Hello, Carl
# Hello, Tom
# Hello, Joe
# Hello, Bob
# Hello, Elsa
print()


def speak(name, phrase):
    print(f"Hello {name}!", end='')
    print(f" {phrase}")


speak(name='John', phrase='Hi, there!')  # Hello John! Hi, there!
# Порядок передачи аргументов важен
speak('Hi, there!', 'John')  # Hello Hi, there!! John
# speak(name='John', told='Hi, there!')  # TypeError: speak() got an unexpected keyword argument 'told'
# speak(name='John')  # TypeError: speak() missing 1 required positional argument: 'phrase'


# Функция с возвратом значений
def speak(name, phrase):
    return f"Hello {name}!" f" {phrase}"  # Возврат типа str


print(speak(name='Tom', phrase='Goodbye'))

# Принтер аргументов args
args = [1, 2, 3, 4, 5]


def args_printer(*args):
    print(type(args))
    print(args)


args_printer('a', 'b', 'c')  # <class 'tuple'> ('a', 'b', 'c')
args_printer(*args)  # <class 'tuple'> (1, 2, 3, 4, 5) Распаковка необходима для передачи аргументов
args_printer(args)  # <class 'tuple'> ([1, 2, 3, 4, 5],)

# Принтер аргументов kwargs
# Ключ в словаре обязательно должен быть типа str иначе будет ошибка TypeError: keywords must be strings
# kwargs = {'Key': 'Value', 1: 1, 2: None} - ошибочно
kwargs = {'Key': 'Value', '1': 1, 'One': None}


def args_printer(**kwargs):
    print(type(kwargs))
    print(kwargs)


args_printer(a='a', b='b', c='c')  # <class 'dict'> {'a': 'a', 'b': 'b', 'c': 'c'}
args_printer(**kwargs)  # <class 'dict'> {'Key': 'Value', '1': 1, 'One': None}
args_printer(kwargs=kwargs)  # <class 'dict'> {'kwargs': {'Key': 'Value', '1': 1, 'One': None}}
# args_printer(kwargs)  # TypeError: args_printer() takes 0 positional arguments but 1 was given
