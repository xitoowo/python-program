class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x * self.x + self.y * self.y


point_1 = Point(1, 2)
# True
print(bool(point_1))  # Функция bool всегда возвращает True для объектов пользовательского класса


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        # Метод __len__ неявно используется в функции bool (Если длина 0 - то False, иначе True)
        return self.x * self.x + self.y * self.y


point_1 = Point(0, 0)
print(bool(point_1))  # False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        # Метод __len__ неявно используется в функции bool (Если длина 0 - то False, иначе True)
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        # Приоритет. Если определен метод __bool__, то именно он используется для расчета
        # В нашем примере проерка равенства x и y
        return self.x == self.y


point_1 = Point(0, 0)
print(bool(point_1))  # True
point_1 = Point(0, 0)
# неявное использование магического метода bool
if point_1:
    print(True)  # True
else:
    print(False)

point_2 = Point(1, 2)

if point_2:
    print(True)
else:
    print(False)  # False
