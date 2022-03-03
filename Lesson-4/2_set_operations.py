# Операции с множествами
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Объединение
# Вввод: {1, 2, 3, 4, 5, 6, 7, 8}
print(a | b)
print(a.union(b))
print(b.union(a))

# Пересечение
# Вввод: {4, 5}
print(a & b)
print(a.intersection(b))
print(b.intersection(a))

# Разница
# Вввод: {4, 5}
print(a - b)  # {1, 2, 3}
print(a.difference(b))  # {1, 2, 3}
print(b.difference(a))  # {8, 6, 7}
print(b - a)  # {8, 6, 7}

# Симметричная разница
# Вввод: {1, 2, 3, 6, 7, 8}
print(a ^ b)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# Остальные операции
# возвращает True, если a является подмножеством b
# Вввод: False
print(a <= b)
print(a.issubset(b))

# возвращает True, если a является надмножеством b
# Вввод: False
print(a >= b)
print(a.issuperset(b))

# возвращает True, если в множествах a и b нет общих элементов
print(a.isdisjoint(b))  # False

a = {1, 2, 3}
b = {4, 5, 6, 7, 8}
print(a.isdisjoint(b))  # True
