import numpy as np

# Одна из ключевых особенностей NumPy – объект ndarray для представления
# N-мерного массива. Это быстрый и гибкий контейнер для хранения больших
# наборов данных в  Python. Массивы позволяют выполнять математические
# операции над целыми блоками данных, применяя такой же синтаксис, как
# для соответствующих операций над скалярами.
# Чтобы показать, как NumPy позволяет производить пакетные вычисления,
# применяя такой же синтаксис, как для встроенных в Python скалярных объектов

# Сгенерировать случайные данные
data = np.random.randn(2, 3)  # 2 списка по 3 элемента
# Список списков выводится без запятых
print(data)  # [[-1.01018305  0.95219617 -0.09589453][ 0.72555213 -1.55185282  1.19211875]]
# Все элементы умножены на 10
print(data * 10)  # [[-10.10183052   9.5219617   -0.95894527][  7.2555213  -15.51852823  11.92118747]]
# Соответственные элементы в  каждой «ячейке» складываются
print(data + data)  # [[-2.0203661   1.90439234 -0.19178905][ 1.45110426 -3.10370565  2.38423749]]

# ndarray – это обобщенный многомерный контейнер для однородных данных, т. е. в нем могут храниться
# только элементы одного типа. У любого массива есть атрибут shape – кортеж, описывающий размер
# по каждому измерению, и  атрибут dtype – объект, описывающий тип данных в  массиве:
print(data.shape)  # (2, 3)
print(data.dtype)  # float64

# Создание ndarray
print()
data = [6, 7.5, 8, 0, 1]
array_1 = np.array(data)
print(array_1)  # [6.  7.5 8.  0.  1. ]
# Вложенные последовательности, например список списков одинаковой длины, можно преобразовать в  многомерный массив:
data = [[1, 2, 3, 4], [5, 6, 7, 8]]
array_2 = np.array(data)
print(array_2)  # [[1 2 3 4] [5 6 7 8]]
# Поскольку data2 – список списков, массив NumPy arr имеет два измерения,
# а его форма выведена из данных. В этом легко убедиться, прочитав атрибуты
# ndim и  shape:
print(array_2.ndim)  # 2
print(array_2.shape)  # (2, 4)
# Если явно не задано противное, то функция np.array пытается самостоятельно определить подходящий тип данных для
# создаваемого массива. Этот тип данных хранится в  специальном объекте dtype. Например, в  примерах выше имеем:
print(array_1.dtype)  # float64
print(array_2.dtype)  # int32

# Помимо np.array существует еще ряд функций для создания массивов. Например, zeros и  ones создают массивы
# заданной длины, состоящие из нулей и  единиц соответственно, а  shape.empty создает массив,
# не инициализируя его элементы. Для создания многомерных массивов нужно передать кортеж, описывающий форму:
print(np.zeros(10))  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(np.zeros((3, 6)))  # [[0. 0. 0. 0. 0. 0.] [0. 0. 0. 0. 0. 0.] [0. 0. 0. 0. 0. 0.]]
# Предполагать, что np.empty возвращает массив из одних нулей, небезопасно.
# Часто возвращается массив, содержащий неинициализированный мусор, как на примере:
# [[[6.23042070e-307 4.67296746e-307]
#   [1.69121096e-306 1.60221072e-306]
#   [3.56043054e-307 7.56595733e-307]]
#
#  [[1.60216183e-306 8.45596650e-307]
#   [1.42417221e-306 1.37961641e-306]
#   [1.60220528e-306 7.56602523e-307]]]
print(np.empty((2, 3, 2)))

# Функция arange – вариант встроенной в Python функции range, только возвращаемым значением является массив:
print(np.arange(15))  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

# Поскольку NumPy ориентирован прежде всего на численные расчеты, тип данных, если он не указан явно,
# во многих случаях предполагается float64 (числа с плавающей точкой).

# Функция Описание
# array
# Преобразует входные данные (список, кортеж, массив или любую другую
# последовательность) в ndarray. Тип dtype задается явно или выводится неявно.
# Входные данные по умолчанию копируются

# asarray
# Преобразует входные данные в ndarray, но не копирует, если на вход уже подан ndarray

# arange
# Аналогична встроенной функции range, но возвращает массив, а не список

# ones, ones_like
# Порождает массив, состоящий из одних единиц, с заданными атрибутами shape
# и dtype. Функция ones_like принимает другой массив и порождает массив из одних
# единиц с такими же значениями shape и dtype

# zeros, zeros_like
# Аналогичны ones и ones_like,только порождаемый массив состоит из одних нулей

# empty, empty_like
# Создают новые массивы, выделяя под них память, но, в отличие от ones и zeros,
# не инициализируют ее

# full, full_like
# Создают массивы с заданными атрибутами shape и dtype, в которых все элементы
# равны заданному символу-заполнителю. full_like принимает массив и порождает
# заполненный массив с такими же значениями атрибутов shape и dtype

# eye, identity
# Создают единичную квадратную матрицу N×N (элементы на главной диагонали равны 1, все остальные – 0


# Тип данных для ndarray
# Тип данных, или dtype, – это специальный объект, который содержит информацию (метаданные),
# необходимую ndarray для интерпретации содержимого блока памяти:
array_1 = np.array([1, 2, 3], dtype=np.float64)
array_2 = np.array([1, 2, 3], dtype=np.int32)
print(array_1.dtype)  # float64
print(array_2.dtype)  # int32

# Числовые dtype именуются единообразно: имя типа, например float или int, затем число, указывающее разрядность одного
# элемента. Стандартное значение с  плавающей точкой двойной точности (хранящееся во внутреннем представлении
# объекта Python типа float) занимает 8 байтов, или 64  бита. Поэтому соответствующий тип в  NumPy называется float64.

# В numpy_datatypes приведен полный список поддерживаемых NumPy типов данных.
# Можно явно преобразовать, или привести, массив одного типа к другому, воспользовавшись методом astype:
int_array = np.array([1, 2, 3, 4, 5])
print(int_array.dtype)  # int32
float_array = int_array.astype(np.float64)
print(float_array.dtype)  # float64
print(int_array)  # [1 2 3 4 5]
print(float_array)  # [1. 2. 3. 4. 5.]

# Перевод из float в int
float_array = np.array([3.7, -1.2, -2.6, 10.1])
print(float_array)  # [ 3.7 -1.2 -2.6 10.1]
int_array = float_array.astype(np.int32)
# Дробная часть отброшена
print(int_array)  # [ 3 -1 -2 10]

# Если имеется массив строк, представляющих целые числа, то astype позволит преобразовать их в числовую форму
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print(numeric_strings)  # [b'1.25' b'-9.6' b'42']
float_strings = numeric_strings.astype(float)
print(float_strings)  # [ 1.25 -9.6  42.  ]

# Будьте осторожнее при работе с типом numpy.string_, поскольку в NumPy размер строковых данных фиксирован и  входные
# данные могут быть обрезаны без предупреждения. Поведение pandas для нечисловых данных лучше согласуется с  интуицией.

# Если по какой-то причине выполнить приведение не удастся (например, если строку нельзя преобразовать в  тип float64),
# то будет возбуждено исключение TypeError. Обратите внимание, что в примере выше float
# вместо np.float64, но NumPy оказался достаточно умным – он умеет подменять типы Python эквивалентными dtype.
# Можно также использовать атрибут dtype другого массива:
int_array = np.array(10)
calibres = np.array([.22, .270, .357, .300, .44, .50], dtype=np.float64)
print(calibres)  # [0.22  0.27  0.357 0.3   0.44  0.5  ]
print(int_array.astype(calibres.dtype))  # 10.0

# На dtype можно сослаться с помощью коротких кодов типа:
empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)  # [2576980378 1074633113  858993459 1072902963 3435973837 1074056396 858993459 1076114227]

# При вызове astype всегда создается новый массив (данные копируются), даже если новый dtype не отличается от старого
