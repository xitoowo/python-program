# Что такое хэш объектов классов, как вычисляется и для чего нужен.
# Переопределение стандартного поведения функции hash() через магические методы __eq__ и __hash__.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point_1 = Point(1, 2)  # объекты пользовательского класса воспринимаются как неизменяемые
point_2 = Point(1, 2)  # и для них можно вычислять хэш
print(hash(point_1))  # 103515271165
print(hash(point_2))  # 103515271159
print(point_1 == point_2)  # False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point_1 = Point(1, 2)
point_2 = Point(1, 2)
# print(hash(point_1))  # unhashable type: 'Point'
# print(hash(point_2))  # unhashable type: 'Point'
print(point_1 == point_2)  # True


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Когда объевляют метод __eq__ 0 функция hash перестает работать TypeError: unhashable type: 'Point'
        # перестает работать стандартный алгоритм вычисления хэша
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


point_1 = Point(1, 2)
point_2 = Point(1, 2)
print(hash(point_1))  # -3550055125485641917
print(hash(point_2))  # -3550055125485641917
print(point_1 == point_2)

data_d = {
    point_1: 1,
    point_2: 2
}

print(data_d)
print(data_d[point_1])
print(data_d[point_2])
