# Срезы строк
# Можно использовать только целочисленные значения 0, 1, 2 ...
# Нельзя 0,5; 2.3 ...
str = 'Hello, Python!'
#
# Печать первого символа
print(f'str[0] = {str[0]}')  # Вывод: H
# Печать последнего символа
print(f'str[-1] = {str[-1]}')  # Вывод: !

# TypeError: string indices must be integers
print(f'str[0.5] = {str[0.5]}')

# IndexError: string index out of range. Выход за пределы строки
print(f'str[15] = {str[15]}')
# IndexError: string index out of range. Выход за пределы строки
print(f'str[-15] = {str[-15]}')

# Стрез со второго элемента по четвертый
# Отсчет начинается с 0
print(f'str[1:5] = {str[1:5]}')  # Вывод: str[1:5] = ello

# Срез с шестого по второй элемент
print(f'str[5:-2] = {str[5:-2]}')  # Вывод: str[5:-2] = , Pytho

# Отрицательный срез
print(f'str[-6:-2] = {str[-6:-2]}')  # Вывод: str[-6:-2] = ytho
