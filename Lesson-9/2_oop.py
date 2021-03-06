# Наследование
# Наследование в объектно-ориентированном программировании очень похоже на наследование в реальной жизни,
# где ребенок наследует те или иные характеристики его родителей в дополнение к его собственным характеристикам.
# Основная идея наследования в объектно-ориентированном программировании заключается в том, что класс может
# наследовать характеристики другого класса. Класс, который наследует другой класс, называется дочерним классом
# или производным классом, и класс, который дает наследие, называется родительским, или основным
# Создание класса Vehicle
class Vehicle:

    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


# Создание класса Car, который наследует Vehicle
class Car(Vehicle):

    def car_method(self):
        print("Это метод из дочернего класса")


car_a = Car()
car_a.car_method()
car_a.vehicle_method()


# Множественное наследование Python
# В Python, родительский класс может иметь несколько дочерних, и, аналогично,
# дочерний класс может иметь несколько родительских классов.
# создаем класс Vehicle
class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


# создаем класс Car, который наследует Vehicle
class Car(Vehicle):
    def car_method(self):
        print("Это дочерний метод из класса Car")


# создаем класс Cycle, который наследует Vehicle
class Cycle(Vehicle):
    def cycle_method(self):
        print("Это дочерний метод из класса Cycle")


car_a = Car()
car_a.vehicle_method()  # вызов метода родительского класса
car_b = Cycle()
car_b.vehicle_method()  # вызов метода родительского класса


# Полиморфизм
# Термин полиморфизм буквально означает наличие нескольких форм. В контексте объектно-ориентированного программирования,
# полиморфизм означает способность объекта вести себя по-разному.
# Полиморфизм в программировании реализуется через перегрузку метода, либо через его переопределение
# создание класса Vehicle
class Vehicle:
    def print_details(self):
        print("Это родительский метод из класса Vehicle")


# создание класса, который наследует Vehicle
class Car(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Car")


# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Cycle")


car_a = Vehicle()
car_a.print_details()

car_b = Car()
car_b.print_details()

car_c = Cycle()
car_c.print_details()


# Инкапсуляция
# Инкапсуляция — это третий столп объектно-ориентированного программирования.
# Инкапсуляция просто означает скрытие данных. Как правило, в объектно-ориентированном программировании один класс
# не должен иметь прямого доступа к данным другого класса.
# Вместо этого, доступ должен контролироваться через методы класса.
# Чтобы предоставить контролируемый доступ к данным класса в Python, используются модификаторы доступа и свойства.

# создаем класс Car
class Car:

    # создаем конструктор класса Car
    def __init__(self, year):
        # Инициализация свойств.
        self.__year = year

    # создаем свойство года.
    @property
    def year(self):
        return self.__year

    # Сеттер для создания свойств.
    @year.setter
    def year(self, year):
        # Проверка на пустое присваивание
        if year:
            self.__year = year


car_a = Car(2018)
print(car_a.year)
car_a.year = 2015
print(car_a.year)
