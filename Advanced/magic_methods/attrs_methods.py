# __new__
# Класс сотрудник
class Employee:
    def __new__(cls, *args, **kwargs):  # cls ссылается на текущий экземпляр класса Employee (на класс)
        # new обязательно должен вернуть адрес нового созданного объекта
        # super по-сути ссылка на базовый класс и из базового класса вызываем new и передаем ему ссылку на на
        # текущий класс Employee
        return super().__new__(cls)

    def __init__(self, name, age, position, place):  # self ссылается на создаваемый экземпляр класса
        self.name = name  # атрибут экземляра класса
        self.age = age
        self.position = position
        self.place = place


# __setattr__, __getattribute__, __getattr__ и __delattr__
# __setattr__(self, key, value)__ - автоматичеки вызывается при изменении свойства key класса
# __getattribute__(self, item) - автоматичеки вызывается при получении свойства класса с именем item
# __getattr__(self, item) - автоматичеки вызывается при получении несуществующего свойства класса с именем item
# __delattr__(self, item) - автоматически вызвается при удалении свойста item (не важно существует или нет)
class EmployeeAttrs:
    def __init__(self, name, age, position, place):
        self.name = name
        self.age = age
        self.position = position
        self.place = place

    def __getattribute__(self, item):  # item атрибут к которому идет обращение
        # Когда идет обращение к кому-либо атрибуту через экземпляр класса, то срабатывает этот метод
        # и возвращает значение соответствующего атрибута

        # Можно управлять общением к любому атрибуту
        print('__getattribute__')
        print(item)
        if item == 'place':
            raise ValueError('Доступ запрещен')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):  # key - имя атрибута, value - новое значение
        if key == 'contract':
            raise AttributeError('Недопустимое значение')
        # self.position = value  # maximum recursion depth exceeded in comparison
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        # При определении этого метода при обращении к несуществующему атрибуту, будет возвращен None
        # Без определения этого метода при обращении к несуществующему атрибуту, будет
        # AttributeError: 'EmployeeAttrs' object has no attribute 'qwe'
        print(f'__getattr__: {item}')

    def __delattr__(self, item):
        print(f'__getattr__: {item}')
        # Без добавления удаления, атрибут останется
        object.__delattr__(self, item)


empl1 = EmployeeAttrs('Xito', 25, 'Dev', '6A')
print(empl1)  # __main__.EmployeeAttrs object at 0x000002BE6B5509A0>
name = empl1.name  # __getattribute__ name
print(name)  # None без return на 34 строке
print(name)  # Xito с return object.__getattribute__(self, item)
# print(empl1.place)  # ValueError: Доступ запрещен
print(empl1.qwe)  # None
