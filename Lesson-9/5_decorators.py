# Декораторы
# Конструктивно декоратор в Python представляет собой некоторую функцию, аргументом которой является другая функция.
# Декоратор предназначен для добавления дополнительного функционала к данной функции без изменения содержимого последней
def first_test():
    print("Test function 1")


def second_test():
    print("Test function 2")


# Мы хотим дополнить их так, чтобы перед вызовом основного кода функции печаталась строка “Run function”,
# а по окончании – “Stop function”.
#
# Сделать это можно двумя способами. Первый – это добавить указанные строки в начало в конец каждой функции,
# но это не очень удобно, т.к. если мы захотим убрать это, нам придется снова модифицировать тело функции.
# А если они написаны не нами, либо являются частью общей кодовой базы проекта, сделать это будет уже не так просто.


def simple_decore(fn):
    def wrapper():
        print("Run function")
        fn()
        print("Stop function")

    return wrapper


first_test_wrapped = simple_decore(first_test)
second_test_wrapped = simple_decore(second_test)

first_test()  # Test function 1
second_test()  # Test function 2
first_test_wrapped()  # Run function Test function 1 Stop function
second_test_wrapped()  # Run function Test function 2 Stop function


# То, что мы только что сделали и является реализацией идеи декоратора. Но вместо строк:

def first_test():
    print("Test function 1")


first_test_wrapped = simple_decore(first_test)
first_test = first_test_wrapped


@simple_decore
def first_test():
    print("Decore function")


first_test()  # Run function Decore function Stop function


# @simple_decore – это и есть декоратор функции.

# Передача аргументов в функцию через декоратор
# Если функция в своей работе требует наличие аргумента, то его можно передать через декоратор.
# Создадим декоратор, который принимает аргумент и выводит информацию о декорируемой функции и ее аргументе.
def param_transfer(fn):
    def wrapper(arg):
        print("Run function: " + str(fn.__name__) + "(), with param: " + str(arg))
        fn(arg)

    return wrapper


# Для демонстрации ее работы создадим функцию, которая выводит квадратный корень переданного ей числа,
# в качестве декоратора, укажем только что созданный param_transfer.
@param_transfer
def print_sqrt(num):
    print(num ** 0.5)


print_sqrt(4)  # Run function: print_sqrt(), with param: 4 2.0


# Возврат результата работы функции через декоратор
# Довольно часто, создаваемые функции возвращают какое-либо значение.
# Для того, чтобы его можно было возвращать через декоратор необходимо соответствующим
# образом построить внутреннюю функцию.

def decor_with_return(fn):
    def wrapper(*args, **kwargs):
        print("Run method: " + str(fn.__name__))
        return fn(*args, **kwargs)

    return wrapper


@decor_with_return
def calc_sqrt(val):
    return val ** 0.5


tmp = calc_sqrt(16)
print(tmp)  # Run method: calc_sqrt 4.0
