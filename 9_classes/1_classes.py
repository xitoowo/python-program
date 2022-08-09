# Классы
# Пустой класс
class Test:
    pass


# Класс сотрудник
class Employee:
    # __init__ Инциализатор класса
    def __init__(self, name, age, position, place):
        self.name = name  # атрибут экземляра класса
        self.age = age
        self.position = position
        self.place = place

    def __del__(self):  # Финализатор класса
        print(f'Удаление экземпляра: {self}')


developer = Employee(name='John', age=40, position='Developer', place='4A')
manager = Employee(name='Joe', age=25, position='Manager', place='5A')
print(developer.name)  # John
print(manager.name)  # Joe


# Атрибуты класса
class Employee:
    all_employees = []  # атрибут класса

    # __init__ инциализатор класса
    def __init__(self, name, age, position, place):
        self.name = name  # атрибут экземляра класса
        self.age = age
        self.position = position
        self.place = place
        # Обращение к атрибуту all_employees и добавление в него экземпляра класса
        self.__class__.all_employees.append(self)


developer = Employee(name='John', age=40, position='Developer', place='4A')
manager = Employee(name='Joe', age=25, position='Manager', place='5A')
print(developer.name)  # John
print(manager.name)  # Joe
print(Employee.all_employees)  # [<__main__.Employee object at 0x000001B384514550>,
# <__main__.Employee object at 0x000001B3845146A0>]
print(len(Employee.all_employees))  # 2


# staticmethod
# Статический метод позволяет избавиться от self в методе те работать не с атрибутами экземпляра класса
# По-сути метод превращается в функцию привязанную к классу
class Calc:
    @staticmethod
    def sum(first_number, second_number):
        return f'Sum: {first_number + second_number}'

    @staticmethod
    def subtraction(first_number, second_number):
        return f'Subtraction: {first_number - second_number}'

    @staticmethod
    def multiplication(first_number, second_number):
        return f'Multiplication: {first_number * second_number}'

    @staticmethod
    def division(first_number, second_number):
        if second_number == 0:
            return 'Error: Division by zero'
        return f'Division: {int(first_number / second_number)}'


print(Calc.sum(8, 6))
print(Calc.subtraction(8, 4))
print(Calc.multiplication(5, 2))
print(Calc.division(10, 5))
print(Calc.division(5, 0))


# classmethod
# Метод класса позволяет работать с атрибутами класса, а не экземпляра
class Vehicle:
    wheels = 4  # Количество колес
    doors = 4  # Количество дверей
    side_mirrors = 3  # Боковые зеркала
    back_mirror = 1

    @classmethod
    def print_technical(cls):
        print(f'Количество колес: {cls.wheels}\nКоличество дверей: {cls.doors}\n'
              f'Количество боковых зеркал: {cls.side_mirrors}\nКоличество зеркал зданего вида: {cls.back_mirror}')


Vehicle.print_technical()

print('-' * 80)


# Переопределение методов
class Vehicle:
    wheels = None  # Количество колес
    doors = None  # Количество дверей
    side_mirrors = None  # Боковые зеркала
    back_mirror = None

    def __init__(self, wheels):
        self.wheels = wheels

    @classmethod
    def print_technical(cls):
        print(f'Количество колес: {cls.wheels}\nКоличество дверей: {cls.doors}\n'
              f'Количество боковых зеркал: {cls.side_mirrors}\nКоличество зеркал зданего вида: {cls.back_mirror}')


# В init переопределили wheels на 4, а все остальные атрибуты (doors, side_mirrors, back_mirror) берутся из класса
vw = Vehicle(4)
print(vw.wheels)  # 4
vw.print_technical()  # Количество колес: None... Количество зеркал зданего вида: None
print(vw.back_mirror)  # None

print('-' * 80)


# Еще один пример с classmethod
class Circle:
    """Класс Circle"""
    all_circles = []
    pi = 3.14

    def __init__(self, r=1):
        """Создать экземпляр Circle с заданным значением radius"""
        self.radius = r
        self.__class__.all_circles.append(self)

    def area(self):
        return self.__class__.pi * self.radius * self.radius

    @classmethod
    def total_area(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total


circle_1 = Circle(3)
circle_2 = Circle(5)
print(circle_1.total_area())  # 106.75999999999999
print(circle_2.total_area())  # 106.75999999999999
print(Circle.total_area())  # 106.75999999999999

