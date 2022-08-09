# Если класс дескриптора содержит только магический метод __get__,
# то он считается non-data descriptor (дескриптор не данных)
# Если в классе помимо магического метода __get__ существуют еще методы __set__ и __del__,
# то он считается data descriptor (дескриптор данных)

class Descriptor:
    def __init__(self):
        self.__vin = None

    # self - ссылка экземпляр класса Descriptor, instance - ссылка на экземпляр класса через который
    # обратились к дескритору, owner - ссылка на класс экзмепляра класса
    def __get__(self, instance, owner):
        return self.__vin

    # self - ссылка на объект с которым происходит работа instance - объект класса из которого был вызван дескриптор
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('VIN должен быть типом str')
        if not value:
            raise TypeError('VIN не должен быть пустым')
        self.__vin = value


class Car:
    list_car = []
    vin = Descriptor()

    def __init__(self, vin=None, model=None, engine=None, brand=None):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.vin = vin
        self.__class__.list_car.append(self)

    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nEngine: {self.engine}"

    @classmethod
    def fast_check(cls, car):
        if car in cls.list_car:
            print('yes')
        else:
            print('no')


a_1 = Car('JTHFE2C24A2504933', "Hyundai", "Solaris", 1.6)
print(a_1.vin)
a_1.vin = 'JTHFE2C24A2504288'
print(a_1)
print(a_1.vin)


class Integer:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('')
        setattr(instance, self.name, value)


class Point:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


point = Point(1, 2, 3)
print(point.__dict__)  # {'__x': 1, '__y': 2, '__z': 3}
print(Integer.__dict__)

