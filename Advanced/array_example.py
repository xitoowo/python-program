# В чем разница между списками и массивами в Python?
# Списки — одна из наиболее распространенных структур данных в Python и основная часть языка.
# Списки и массивы ведут себя сходным образом.
# Как и массивы, списки представляют собой упорядоченную последовательность элементов.
# Они также изменяемы и не имеют фиксированного размера, то есть могут увеличиваться и
# уменьшаться на протяжении всей жизни программы. Элементы можно добавлять и удалять,
# что делает списки очень гибкими в работе.
# Однако списки и массивы — это не одно и то же.
# В списках могут храниться элементы различных типов данных.
# Это означает, что список может одновременно содержать целые числа, числа с плавающей запятой,
# строки или любой другой тип данных Python. С массивами это не сработает.
# Как уже упоминалось, массивы хранят элементы только какого-то одного типа данных.
# Это важно помнить! Есть массивы целых чисел, массивы чисел с плавающей запятой и т.д.

# Когда следует использовать массивы в Python
# Списки встроены по умолчанию в язык программирования Python, а массивы — нет.
# Поэтому, если вы хотите использовать массивы, их сперва нужно импортировать через модуль array.
#
# Массивы модуля array представляют собой тонкую обертку массивов в C.
# Они полезны, когда вам нужно работать с однородными данными.
#
# Они также более компактны и занимают меньше памяти и места, что делает их более эффективными по сравнению со списками.
#
# Если вы хотите выполнять математические вычисления, лучше воспользоваться массивами NumPy, импортировав модуль NumPy.
#
# Стоит отметить, что использовать массивы в Python следует только тогда,
# когда вам это действительно нужно, ведь списки работают аналогичным образом и более гибки в работе.
import array as arr
# TYPECODE	ТИП В C	            ТИП В PYTHON	    РАЗМЕР
# ‘b’	    signed char	        int	                1
# ‘B’	    unsigned char	    int	                1
# ‘u’	    wchar_t	            Unicode character	2
# ‘h’	    signed short	    int	                2
# ‘H’	    unsigned short	    int	                2
# ‘i’	    signed int	        int	                2
# ‘I’	    unsigned int	    int	                2
# ‘l’	    signed long	        int	                4
# ‘L’	    unsigned long	    int	                4
# ‘q’	    signed long long	int	                8
# ‘Q’	    unsigned long long	int	                8
# ‘f’	    float	            float	            4
# ‘d’	    double	            float	            8
numbers = arr.array('i', [10, 20, 30])  # Вывод: array('i', [10, 20, 30])
print(numbers)
print(numbers[0])  # Получение 1-го элемента 10
print(numbers[1])  # Получение 2-го элемента 20
print(numbers[2])  # Получение 3-го элемента 30
print(numbers[-1])  # Получение последнего элемента 30
print(numbers[-2])  # Получение предпоследнего элемента 20
print(numbers[-3])  # Получение первого элемента 10
# Поиск индекса элемента со значением 10
print(numbers.index(10))  # Вывод: 0

for number in numbers:
    print(number)  # Вывод: 10 20 30

# Получение только значений 10 и 20
print(numbers[:2])  # С первой по вторую позицию (индексы 0 и 1). Вывод: array('i', [10, 20])
# В остальном они схожи со списками и можно использовать append, extend, insert, pop, remove, etc ...

# Массив чисел с плавающей запятой
numbers = arr.array('d', [10.0, 20.0, 30.0])  # Вывод: array('d', [10.0, 20.0, 30.0])
print(numbers)
print(len(numbers))  # Вывод: 3
