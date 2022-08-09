class Circle:
    all_circles = []
    pi = 3.14

    def __init__(self, r=1):
        self.radius = r
        self.__class__.all_circles.append(self)

    def __str__(self):
        return f'{self.radius}'

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def area(self):
        return self.__class__.pi * self.radius * self.radius

    @classmethod
    def total_area(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total

    @staticmethod
    def print_class_name():
        print('Circle')


circle_1 = Circle(3)
circle_2 = Circle(5)
circle_3 = Circle()

print(circle_1)
print(circle_2)
print(circle_3)

print(Circle.all_circles)

