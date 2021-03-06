# Профилирование эффективности генератора
# Ранее мы узнали, что использование генераторов является отличным способом оптимизации памяти.
# И хотя генератор бесконечной последовательности является наиболее ярким примером этой оптимизации,
# давайте рассмотрим еще один пример с возведением числа в квадрат и проверим размер полученных объектов.
#
# Вы можете сделать это с помощью вызова функции sys.getsizeof ():
# Функция getsizeof() модуля sys возвращает размер объекта object в байтах.
import sys

nums_squared_lc = [i * 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc)  # 87624
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))  # 120

# В этом случае размер списка, полученного с помощью выражения составляет 87 624 байта,
# а размер генератора — только 120. То есть, список занимает памяти в 700 раз больше, чем генератор!
# Однако нужно помнить одну вещь. Если размер списка меньше доступной памяти на работающей машине,
# тогда обработка его будет занимать меньше времени, чем аналогичная обработка генератора. Чтобы удостовериться в этом,
# давайте просуммируем результаты приведенных выше выражений.
# Вы можете использовать для анализа функцию cProfile.run ():

import cProfile

cProfile.run('sum([i * 2 for i in range(10000)])')
#       5 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.001    0.001 <string>:1(<listcomp>)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('sum((i * 2 for i in range(10000)))')
#       10005 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  10001    0.002    0.000    0.002    0.000 <string>:1(<genexpr>)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1    0.001    0.001    0.003    0.003 {built-in method builtins.sum}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Здесь вы можете видеть, что суммирование всех значений, содержащихся в списке заняло около трети времени аналогичного
# суммирования с помощью генератора. Поэтому если скорость является для вас проблемой, а память — нет, то список,
# возможно, окажется лучшим инструментом для работы.
#
# Примечание. Эти измерения действительны не только для генераторов, созданных с помощью выражений.
# Они абсолютно идентичны и для генераторов, созданных с помощью функции.
# Ведь, как мы уже говорили выше, эти генераторы эквивалентны.
#
# Запомните, что выражения создающие списки возвращают списки,
# в то время как выражения генераторов возвращают генераторы. Генераторы работают одинаково, независимо от того,
# построены они на основе функции или выражения. Использование выражения позволяет вам задать простые генераторы
# одной строкой и также предполагает yield в конце каждой итерации. Ключевое слово yield, безусловно, является основой,
# на которой основывается вся функциональность генераторов.

# Сравнение операторов yield и return в Python (с примерами)
# Функция, содержащая yield, может генерировать сразу несколько результатов. Она приостанавливает выполнение программы,
# отправляет значение результата вызывающей стороне и возобновляет выполнение с последнего yield. Кроме того, функция,
# содержащая yield, отправляет сгенерированную серию результатов в виде объекта-генератора.
#
# Return также является встроенным ключевым словом в Python. Он завершает функцию,
# а вызывающей стороне отправляет значение.

# Разница между yield и return
# Начнем с того, что между yield и return есть много заметных различий. Для начала давайте обсудим их.
#
# RETURN
# Оператор return возвращает только одно значение.
# Return выходит из функции, а в случае цикла он закрывает цикл.Это последний оператор, нужно разместить внутри функции.
# Логически, функция должна иметь только один return.
# Оператор return может выполняться только один раз.
# Return помещается внутри обычной функции Python.

# YIELD
# Оператор yield может возвращать серию результатов в виде объекта-генератора.
# Не уничтожает локальные переменные функции. Выполнение программы приостанавливается,
# значение отправляется вызывающей стороне, после чего выполнение программы продолжается с
# последнего оператора yield.
# Внутри функции может быть более одного оператора yield.
# Оператор yield может выполняться несколько раз.
# Оператор yield преобразует обычную функцию в функцию-генератор.

# Теперь давайте рассмотрим разницу между операторами return и yield на примерах.
#
# В приведенном ниже коде мы использовали несколько операторов возврата.
# Вы можете заметить, что выполнение программы прекратится уже после первого оператора return.
# Весь код, идущий после, не будет выполнен.

num1 = 10
num2 = 20


def mathOP():
    return num1 + num2
    return num1 - num2
    return num1 * num2
    return num1 / num2


print(mathOP())

# В выводе видно, что функция возвращает только первое значение, после чего программа завершается.
#
# Чтобы выполнить аналогичную задачу с несколькими операторами return,
# нам нужно создать четыре разные функции для каждого типа арифметической операции.

num1 = 10
num2 = 20


def sumOP():
    return num1 + num2


def subtractOP():
    return num1 - num2


def multiplicationOP():
    return num1 * num2


def divisionOP():
    return num1 / num2


print("The sum value is: ", sumOP())
print("The difference value is: ", subtractOP())
print("The multiplication value is: ", multiplicationOP())
print("The division value is: ", divisionOP())

# Запустив данный код, получим следующий результат:
# Однако мы можем выполнить эти арифметические операции внутри одной функции-генератора,
# используя несколько операторов yield.

num1 = 10
num2 = 20


def mathOP():
    yield num1 + num2
    yield num1 - num2
    yield num1 * num2
    yield num1 / num2


print("Printing the values:")
for i in mathOP():
    print(i)

# Давайте рассмотрим еще один пример использования операторов return и yield.
# Давайте рассмотрим еще один пример использования операторов return и yield.
# Создадим список чисел и передадим его в функцию mod() в качестве аргумента. Далее, внутри функции,
# мы проверяем каждый элемент списка. Если он делится без остатка на 10, то мы его выводим.
# Для начала давайте реализуем этот пример в нашем скрипте Python с использованием оператора return.
myList = [10, 20, 25, 30, 35, 40, 50]


def mod(myList):
    for i in myList:
        if (i % 10 == 0):
            return i


print(mod(myList))
# Оператор return возвращает только первое число, кратное 10, и завершает выполнение функции.
# Теперь давайте реализуем тот же пример, используя оператор yield.
myList = [10, 20, 25, 30, 35, 40, 50]


def mod(myList):
    for i in myList:
        if (i % 10 == 0):
            yield i


for i in mod(myList):
    print(i)

# И return, и yield являются встроенными ключевыми словами (или операторами) Python.
# Оператор return используется для возврата значения из функции. При этом он прекращает выполнение программы.
# А оператор yield создает объект-генератор и может возвращать несколько значений, не прерывая выполнение программы.
