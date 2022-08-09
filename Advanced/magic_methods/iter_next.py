# __iter__(self) - получение итератора для переборки объекта
# __next__(self) - переход к следующему значению и его считывание
# любой список, например список это итерируемый объект, поэтому для него мы можем создать итератор
# те некий интерфейс для перебора элементов любого итерируемого объекта, в данном случае списка
# Затем последовательно вызываем функцию next() и соответсвтвенно читаем последующие элементы итерируемого объекта
my_list = [1, 2, 3, 4, 5]
print(list(range(5)))  # функция list(), автоматически внутри себя перебрала все элементы функции range
a = iter(range(5))
print(next(a))  # 0
print(next(a))  # 1
print(next(a))  # 2
print(next(a))  # 3
print(next(a))  # 4
# print(next(a))  # StopIteration


class Frange:  # генерация арифмитической последовательности вещественных чисел
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop  # доходя до stop, но не включая его
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:  # self.value + self.step - первое значение арифм последовательности
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = Frange(0, 2, 0.5)
print(fr.__next__())  # 0.0
print(next(fr))  # 0.5
print(fr.__next__())  # 1.0
print(fr.__next__())  # 1.5
# print(fr.__next__())  # StopIteration
# Итератор это объект у которого объявлен метод __next__, который неявно вызывается


# for i in fr: print(i)  # TypeError: 'Frange' object is not iterable
# Для использования объекта в цикле, необходимо добавить магический метод __iter__
class Frange:  # генерация арифмитической последовательности вещественных чисел
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop  # доходя до stop, но не включая его
        self.step = step

    def __iter__(self):
        # каждый раз при вызове функции iter(), self.value будет инициализироваться на начало
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:  # self.value + self.step - первое значение арифм последовательности
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = Frange(1, 3, 0.5)
for x in fr:  # iter вызывается внутри for
    print(x)
