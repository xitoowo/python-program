# __getitem__(self, item) - получение значения по ключу item
# __setitem__(self, key, value) - запись значения value по ключу key
# __delitem__(self, key) - удаление элемента по ключу
class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks


student = Student('Oleg', [5, 3, 5, 2, 3])
print(student.marks[0])  # 5


# Что если мы хотим получить оценку через такое обращение student[0]
# print(student[0])  # TypeError: 'Student' object is not subscriptable
class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]


student = Student('Oleg', [5, 3, 5, 2, 3])
print(student[1])  # 3


class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        # Можно прописывать свою логику и свои проверки
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')


student = Student('Oleg', [5, 3, 5, 2, 3])
print(student[0])
# print(student[10])  # IndexError: Неверный индекс


# Чтое сли бы мы хотели изменять оценки таким же способом student[0] = 4
# student[0] = 4  # TypeError: 'Student' object does not support item assignment
class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        # Можно прописывать свою логику и свои проверки
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Индекс должен быть целым положительным числом')
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)  # расширение списка на off
        self.marks[key] = value


student = Student('Oleg', [5, 3, 5, 2, 3])
print(student.marks)  # [5, 3, 5, 2, 3]
student[0] = 4
print(student.marks)  # [4, 3, 5, 2, 3]
# student[-2] = 4  # TypeError: Индекс должен быть целым положительным числом
student[10] = 4
print(student.marks)  # [4, 3, 5, 2, 3, None, None, None, None, None, 4]


class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        # Можно прописывать свою логику и свои проверки
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Индекс должен быть целым положительным числом')
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)  # расширение списка на off
        self.marks[key] = value

    def __delitem__(self, key):
        # вызывается когда происходит удаление элемента
        self.marks.pop(key)  # удаление по индексу!


student = Student('Oleg', [5, 3, 5, 2, 3])
print(student.marks)  # [5, 3, 5, 2, 3]
student[0] = 4
print(student.marks)  # [4, 3, 5, 2, 3]
# student[-2] = 4  # TypeError: Индекс должен быть целым положительным числом
student[10] = 4
print(student.marks)  # [4, 3, 5, 2, 3, None, None, None, None, None, 4]
del student[9]
print(student.marks)  # [4, 3, 5, 2, 3, None, None, None, None, 4]
