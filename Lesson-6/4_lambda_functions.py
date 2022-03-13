# Lambda-функция позволяет нам определять функцию анонимно.
# лямбда-функция возвращает значение, и у нее есть неявный оператор return.
# Пример с filter
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 3 == 0, numbers))
print(result)  # [0, 3, 6, 9]

# Пример с map
result = list(map(lambda x: x % 3 == 0, numbers))
print(result)  # [True, False, False, True, False, False, True, False, False, True, False]

# Пример с reduce
from functools import reduce

result = reduce(lambda x, y: y - x, numbers)
print(result)  # 5
# 1 - 0 = 1
# 2 - 1 = 1
# 3 - 1 = 2
# 4 - 2 = 2
# 5 - 2 = 3
# 6 - 3 = 3
# 7 - 3 = 4
# 8 - 4 = 4
# 9 - 4 = 5
# 10 - 5 = 5
