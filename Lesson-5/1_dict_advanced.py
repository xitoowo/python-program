# Операции словарей
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# По умолчанию in проверят существует ли ключ
print(1 in squares)  # True
print(9 in squares)  # False
print(9 not in squares)  # True
# Такая же запись
print(1 in squares.keys())  # True
print(9 in squares.keys())  # False
print(9 not in squares.keys())  # True

# Проверка сущетсвует ли значение
print(1 in squares.values())  # True
print(9 in squares.values())  # True
print(36 not in squares.values())  # True

# Проверка сущетсвует ли пара ключ:значение
# Формат (1, 1) потому что items возвращает кортеж (ключ, значение)
print((1, 1) in squares.items())  # True
print((5, 25) in squares.items())  # True
print((5, 20) in squares.items())  # False
print((6, 36) in squares.items())  # False


# Генераторы словарей
squares = {x: x*x for x in range(11)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)  # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Проход по словарю
for x, y in odd_squares.items():
    print(x, y)

# 1 1
# 3 9
# 5 25
# 7 49
# 9 81
