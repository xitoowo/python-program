# Класс функтора
class Counter:
    def __init__(self):
        self.__counter = -4

    def __call__(self, *args, **kwargs):
        self.__counter -= 1
        return self.__counter


counter = Counter()
counter_value = counter()
print(counter_value)
value = -5
print(value is counter_value)


