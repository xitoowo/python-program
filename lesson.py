# Магические или dunder методы
import functools


class Number:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def to_string(first_number, second_number):
        return str(first_number) + str(second_number)

    def update(self, index, other):
        number_list = [x for x in str(self.value)]
        number_list[index] = other
        result = functools.reduce(Number.to_string, number_list)
        self.value = int(result)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'Number({self.value})'

    def __eq__(self, other):
        # Определяет поведение оператора ==
        if isinstance(other, Number):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        if isinstance(other, list):
            result = [int(x) for x in str(self.value)]
            return result == other
        raise TypeError('Тип данных не поддерживается')

    def __lt__(self, other):
        # Определяет поведение оператора <
        if isinstance(other, Number):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        raise TypeError('Тип данных не поддерживается')

    def __gt__(self, other):
        # Определяет поведение оператора >
        if isinstance(other, Number):
            return self.value > other.value
        if isinstance(other, int):
            return self.value > other
        raise TypeError('Тип данных не поддерживается')

    def __le__(self, other):
        # Определеяет поведение оператора <=
        if isinstance(other, Number):
            return self.value <= other.value
        if isinstance(other, int):
            return self.value <= other
        raise TypeError('Тип данных не поддерживается')

    def __ge__(self, other):
        # Определяет поводение оператора >=
        if isinstance(other, Number):
            return self.value >= other.value
        if isinstance(other, int):
            return self.value >= other
        raise TypeError('Тип данных не поддерживается')


number_1 = Number(4586)
number_2 = Number(4789)
print(number_1)
print(number_1 == [4, 5, 8, 6])
print(number_1 == number_2)
print(number_1 < number_2)
print(number_1 > 0)
print(number_1 > False)
print(number_1 > number_2)
