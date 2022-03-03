# Bool
# Логический тип представлен двумя постоянными значениями False и True.
# Значения используются для представления истинности.
# Можно представить, как False - 0, True - 1
# Подтип int
print(bool(0))  # Вывод: False
print(bool(1))  # Вывод: True

# Сравнение
# В данном примере возвращается True/False в зависимости от равенства, if использовать необязательно
print(True == 0)  # Вывод: False
print(False == 1)  # Вывод: False

# Можно сравнивать с другими числами
print(True > 0)  # Вывод: True
print(False <= 0)  # Вывод: True
print(True > 2)  # Вывод: True
print(False <= 10)  # Вывод: True

# Bool с другими значениями
print(bool(''))  # Вывод: False
print(bool('string'))  # Вывод: True
print(bool(10))  # Вывод: True
print(bool(-10))  # Вывод: True
print(bool(5.5))  # Вывод: True
print(bool(-9.8))  # Вывод: True
