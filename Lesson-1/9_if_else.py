# Условная инструкция if-elif-else (оператор ветвления)
# Любое число, не равное 0, или непустой объект - истина.
# Числа, равные 0, пустые объекты и значение None - ложь
# Операции сравнения применяются к структурам данных рекурсивно
# Операции сравнения возвращают True или False
# Логические операторы and и or возвращают истинный или ложный объект-операнд

# Простая программа на понимание условий. Если введенное число == 5, то выводится надпись "Вы угадали число!"
print('Угадай число')
a = int(input('Введите число: '))
# 5 - искомое число
if a == 5:
    print('Вы угадали число!')
else:
    print('Введите другое число!')

# Обновленная версия с несколькими числами
print('Угадай число')
a = int(input('Введите число: '))
# 5, 55 - искомые число
if a == 5:
    print('Вы угадали число!')
elif a == 55:
    print('Вы угадали число!')
else:
    print('Введите другое число!')

# Использование или.
print('Угадай число')
a = int(input('Введите число: '))
# 5, 55 - искомые число
if a == 5 or a == 55:
    print('Вы угадали число!')
else:
    print('Введите другое число!')

# Использование и.
print('Угадай число')
a = int(input('Введите число: '))
b = int(input('Введите число: '))
# 5, 55 - искомые число
if a == 5 and b == 55:
    print('Вы угадали число!')
else:
    print('Введите другое число!')

# Что будет если пользователь введет не число, а букву
# ValueError: invalid literal for int() with base 10: 'f'
print('Угадай число')
a = input('Введите число: ')
b = input('Введите число: ')
if not a.isdigit() or b.isdigit():
    print('Введите число, а не строчку!')
    exit()
# 5, 55 - искомые число
if int(a) == 5 and int(b) == 55:
    print('Вы угадали число!')
else:
    print('Введите другое число!')

# или
print('Угадай число')
a = input('Введите число: ')
b = input('Введите число: ')
if a.isdigit() and b.isdigit():
    # 5, 55 - искомые число
    if int(a) == 5 and int(b) == 55:
        print('Вы угадали число!')
    else:
        print('Введите другое число!')
else:
    print('Введите число, а не строчку!')
