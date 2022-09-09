# Модуль dataclasses в Python, создание типов данных.
# Упрощенное создание пользовательских типов данных.
# Модуль dataclasses предоставляет декоратор и функции для автоматического добавления сгенерированных специальных
# методов, таких как __init__() и __repr__(), в определяемые пользователем классы.
#
# Атрибуты класса - переменные для использования в этих сгенерированных методах определяются с
# использованием аннотаций типов.
#
# Пример:


from dataclasses import dataclass


@dataclass
class InventoryItem:
    """Класс для отслеживания товара."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


#
# Декоратор @dataclass помимо прочего, добавит метод __init__(), который будет выглядеть так:
#
# def __init__(self, name: str, unit_price: float, quantity_on_hand: int=0):
#     self.name = name
#     self.unit_price = unit_price
#     self.quantity_on_hand = quantity_on_hand
# Обратите внимание, что этот метод автоматически добавляется в класс: он не прописывается вручную в показанном
# выше определении класса InventoryItem(). Такое поведение облегчает написание небольших классов,
# представляющих из себя пользовательские типы, предназначенные для упорядоченного хранения нестандартных данных.
#
# Обработка после инициализации, метод __post_init__().
# Сгенерированный код __init__() вызовет специальный метод с именем __post_init__(), если __post_init__()
# определен в классе. Обычно он называется self.__post_init__ ().
#
# Если определены какие-либо поля InitVar, они также будут переданы в __post_init__() в том порядке,
# в котором они были определены в классе. Если метод __init__() не сгенерирован, то __post_init__() не будет
# вызываться автоматически.
#
# Такое поведение позволяет инициализировать значения полей, которые зависят от одного или нескольких
# других полей. Например:

from dataclasses import dataclass, field


@dataclass
class MyType:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b


mytype = MyType(7, 9)
# mytype MyType(a=7, b=9, c=16)

# Переменные (поля) класса данных.
# Одно из двух мест, где функция-декоратор dataclasses.dataclass() фактически проверяет тип поля - это определение того,
# является ли поле переменной класса. В этом случае функция-декоратор проверяет,
# является ли тип поля типизированным typing.ClassVar.
#
# Если поле типизировано typing.ClassVar, то оно исключается из рассмотрения как поле и игнорируется механизмами класса
# данных. Такие псевдо-поля ClassVar не возвращаются функцией модуля dataclasses.fields().
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class MyType:
    x: int
    y: int
    n: ClassVar


# >>> mytype = MyType(7, 9)
# >>> mytype
# # MyType(x=7, y=9)
#
# # присвоим переменной класса `d` значение
# >>> mytype.d = 5
# # переменная `d` игнорируется механизмами
# # класса данных и не будет видна как поле
# >>> mytype
# # Point(x=7, y=9)
#
# # хотя со значением `d` можно работать
# >>> mytype.d
# # 5

# Переменные (поля) только для инициализации InitVar.
# Другое место, где функция-декоратор dataclasses.dataclass() проверяет аннотацию типа, - это определение, является
# ли поле переменной только для инициализации.
#
# Он делает это, проверяя, имеет ли тип поля тип dataclasses.InitVar. Если поле является InitVar, то оно считается
# псевдополем, которое называется полем только для инициализации. Поскольку это не истинное поле, оно не возвращается
# функцией fields() уровня модуля. Поля только для инициализации добавляются в качестве параметров
# к сгенерированному методу __init__() и передаются в необязательный метод __post_init__().
# По другому они не используются классами данных.
#
# Например, предположим, что поле будет инициализировано из базы данных, если значение не указано при создании класса:

@dataclass
class MyType:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')


mytype = MyType(10, database=my_database)


#
# В этом случае dataclasses.fields() вернет объекты Field для i и j, но не для базы данных.
#
# Замороженные (неизменяемые) экземпляры класса.
# Невозможно создать действительно неизменяемые объекты Python, но, передав Frozen=True
# декоратору dataclasses.dataclass(), можно эмулировать неизменяемость. В этом случае классы данных добавят к классу
# методы __setattr__() и __delattr__(). При вызове эти методы вызывают ошибку dataclasses.FrozenInstanceError.
#
# При использовании аргумента frozen=True наблюдается небольшое снижение производительности: __init__() не может
# использовать простое присваивание для инициализации полей и должен использовать object.__setattr__().


@dataclass(frozen=True)
class MyType:
    x: int
    y: int


# >>> mytype = MyType(7, 9)
# >>> mytype
# # Point(x=7, y=9)
# >>> mytype.x = 15
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<string>", line 4, in __setattr__
# dataclasses.FrozenInstanceError: cannot assign to field 'x'

# Наследование.
# Когда класс данных создается декоратором dataclasses.dataclass(), он просматривает все базовые классы класса в
# обратном MRO (то есть начиная с объекта) и для каждого найденного класса данных добавляет поля этого базового
# класса в упорядоченное отображение полей.
#
# После добавления всех полей базового класса он добавляет свои собственные поля к упорядоченному отображению.
# Все сгенерированные методы будут использовать это комбинированное вычисляемое упорядоченное сопоставление полей.
# Поскольку поля расположены в порядке вставки, производные классы переопределяют базовые классы. Например:
from dataclasses import dataclass
from typing import Any


@dataclass
class Base:
    x: Any = 15.0
    y: int = 0


@dataclass
class MyType(Base):
    z: int = 10
    x: int = 15


# Окончательный список полей в порядке x, y, z. Последний тип x будет int, как указано в классе MyType.
#
# Сгенерированный метод __init__() для MyType будет выглядеть так:
# def __init__(self, x: int = 15, y: int = 0, z: int = 10):

# Фабричные функции по умолчанию.
# Если функция dataclasses.field() использует аргумент default_factory, то он вызывается с нулевыми аргументами,
# когда требуется значение по умолчанию для поля.
#
# Например, чтобы создать новый экземпляр списка, используйте:

from dataclasses import dataclass, field


@dataclass
class MyType():
    x: int
    mylist: list = field(default_factory=list)


# >>> mytype = MyType(9)
# >>> mytype1 = MyType(9, [10, 20, 30])
# >>> mytype
# # MyType(x=9, mylist=[])
# >>> mytype1
# # MyType(x=9, mylist=[10, 20, 30])

# Если поле исключено из __init__() (с использованием init=False) и в поле также указывается default_factory,
# то тогда фабричная функция по умолчанию всегда будет вызываться из сгенерированной функции __init__().
# Это происходит потому, что другого способа присвоить полю начальное значение нет.
#
# Изменяемые значения по умолчанию.
# Python сохраняет значения переменных-членов по умолчанию в атрибутах класса.
# Рассмотрим класс типа данных, который не использует модуль dataclasses:

class MyType:
    x = []

    def add(self, element):
        self.x.append(element)


# >>> o1 = MyType()
# >>> o2 = MyType()
# >>> o1.add(1)
# >>> o2.add(2)
# >>> assert o1.x == [1, 2]
# >>> assert o1.x is o2.x

# Обратите внимание, что такой код имеет проблему - два экземпляра класса MyType, которые не указывают значение
# для x при создании экземпляра класса, будут использовать одну и ту же копию списка x.
#
# Что бы защитить себя от таких ошибок, при создании классов для хранения данных используйте модуль dataclasses и
# декоратор @dataclass. Если написать код, эквивалентный предыдущему примеру с использованием @dataclass,
# то при создании экземпляра класса MyType() просто поднимется исключение.

from dataclasses import dataclass


@dataclass
class MyType:
    x: list = []

    def add(self, element):
        self.x += element


# >>> mytype = MyType()
# Traceback (most recent call last):
# ...
#     raise ValueError(f'mutable default {type(f.default)} for field '
# ValueError: mutable default <class 'list'> for field x is not allowed: use default_factory
# Классы данных вызывают ошибку ValueError, если обнаруживают параметр по умолчанию list, dict или set.
# Это частичное решение, но оно защищает от многих проблем.
#
# При создании типов данных, которые используют в качестве полей изменяемые последовательности
# используйте фабричные функций по умолчанию:
from dataclasses import dataclass, field


@dataclass
class MyType:
    x: list = field(default_factory=list)

    def add(self, element):
        self.x += element


# >>> assert D().x is not D().x
# Поля только для ключевых слов.
# С версии Python 3.10 модуль dataclasses поддерживает поля, содержащие только ключевые слова в сгенерированном
# методе __init__(). Есть несколько способов указать поля, содержащие только ключевые слова.
#
# Можете определить в конструкторе, что каждое поле содержит только ключевые слова:

from dataclasses import dataclass
import datetime


@dataclass(kw_only=True)
class Birthday:
    name: str
    birthday: datetime.date


#
# И name, и birthday являются только ключевыми аргументами для сгенерированного метода __init__().
# Можно указать только ключевые слова для каждого поля:


@dataclass
class Birthday:
    name: str
    birthday: datetime.date = field(kw_only=True)


# Здесь только birthday - только ключевое слово. Если устанавливать kw_only для отдельных полей, то нужно иметь в виду,
# что существуют правила переупорядочения полей из-за того, что поля, содержащие только ключевые аргументы.
# Эти поля должны следовать за полями, не содержащими ключевые аргументы.
#
# Также можно указать, что все поля, следующие за маркером KW_ONLY, содержат только ключевые аргумента.
# Скорее всего, это будет наиболее распространенное использование:

from dataclasses import dataclass, KW_ONLY


@dataclass
class Point:
    x: float
    y: float
    _: KW_ONLY
    z: float = 0.0
    t: float = 0.0

# Здесь z и t являются параметрами только для ключевых слов, а x и y - нет.
