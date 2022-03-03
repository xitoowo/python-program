class Test:
    def __init__(self, name, salary):
        self.v1 = name
        self.v2 = salary


val = Test('John', 50000)
print(val.__str__())  # <__main__.Test object at 0x000001B483582FD0>. repr выполняет функцию str
print(val.__repr__())  # <__main__.Test object at 0x000001B483582FD0>


class User:
    def __init__(self, name, salary):
        self.v1 = name
        self.v2 = salary

    def __str__(self):
        return f'User name is {self.v1} and salary is {self.v2}'

    def __repr__(self):
        return f'User(name={self.v1}, salary={self.v2})'


val = User('John', 50000)
print(val.__str__())  # User name is John and salary is 50000. Красивый вывод при print
print(val.__repr__())  # User(name=John, salary=50000). Представление, как создать объект

# Динамическое исполнение выражений из ввода на основе строки
# eval()может сделать ваш код небезопасным, предположим, что вы хотите создать онлайн-сервис для оценки
# произвольных выражений Python. Ваш пользователь вводит выражения и нажимает кнопку «Выполнить».
# Приложение получает пользовательский ввод и передает его для выполнения в eval() .
# Если вы используете Linux и приложения имеет необходимые разрешения,
# то злонамеренный пользователь может ввести опасную строку, подобную следующей:
# "__import__('subprocess').getoutput('rm –rf *')"
# Выполнение выражения удалит все файлы в текущей директории.
# https://proglib.io/p/dinamicheskoe-vypolnenie-vyrazheniy-v-python-funkciya-eval-2020-05-14
bob = eval('User("Bob", 2000)')  # User name is Bob and salary is 2000
print(bob)
print(bob.v1)  # Bob
print(bob.v2)  # 2000
