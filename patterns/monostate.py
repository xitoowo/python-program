# Класс, у которого объекты имеют единое локальное пространство, единые локальные атрибуты - паттерн "Моносостояние".

class Mono:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        # Переопределняем ссылку экземпляра на общий словарь атрибутов
        self.__dict__ = self.__shared_attrs

    def __str__(self):
        return f'{self.__shared_attrs}'


th1 = Mono()
th2 = Mono()
print(th1)  # {'name': 'thread_1', 'data': {}, 'id': 1}
print(th2)  # {'name': 'thread_1', 'data': {}, 'id': 1}
th2.name = 'QQQ'
print(th1)  # {'name': 'QQQ', 'data': {}, 'id': 1}
print(th2)  # {'name': 'QQQ', 'data': {}, 'id': 1}
th1.new_attrs = 'new_attrs'
print(th1)  # {'name': 'QQQ', 'data': {}, 'id': 1, 'new_attrs': 'new_attrs'}
print(th2)  # {'name': 'QQQ', 'data': {}, 'id': 1, 'new_attrs': 'new_attrs'}
