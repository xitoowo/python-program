class Descriptor:
    def __init__(self):
        self.__vin = None

    def __get__(self, instance, owner):
        return self.__vin

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('VIN должен быть типом str')
        if not value:
            raise TypeError('VIN не должен быть пустым')
        self.__vin = value


class Car:
    list_car = []
    __vin = Descriptor()

    def __init__(self, vin=None, model=None, engine=None, brand=None):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.__vin = vin
        self.__class__.list_car.append(self)

    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nEngine: {self.engine}"

    @property
    def vin(self):
        return self.__vin

    @vin.setter
    def vin(self, other):
        if len(other) != 17:
            raise Exception('Длина VIN должна быть в рамках 17 символов')
        self.__vin = other

    @vin.getter
    def vin(self):
        return f'VIN: {self.__vin}'

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
