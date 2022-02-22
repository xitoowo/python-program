# Цикл For
# для <каждого элемента> в <последовательности>:
#     <выполняем тело цикла>
for index in range(10):
    print(index)  # Вывод:  0 1 2 3 4 5 6 7 8 9
print()
# Итерация по списку
# C-подобная
nums = [1, 2, 3, 4, 5, 6, 7]
# Функция len позволяет узнать размер (длину) списка
for i in range(len(nums)):
    # Происходит обращение к списку по индексу
    print(nums[i])
print()
# Range
# Функция range генерирует список от 0 до конца и проходит по нему
# Синтаксис range(начало, конец, шаг)
# Шаг может быть положительным, отрицательным, но не 0
# Положительный
for index in range(0, 10, 2):
    print(index, end='')  # Вывод:  0 2 4 6 8
print()
# Отрицательный
# Для этого необходимо указать конец > начала
for index in range(20, 10):
    print(index)  # Вывод:  20 18 16 14 12
print()
for index in range(20, 10, -2):
    print(index)  # Вывод:  18 16 14 12
print()
# В Python сущетсвует возможность итерироваться по элементам напрямую
for num in nums:
    print(num)
print()
n = 3
print(n)  # Вывод: 3
# Временная переменная n в теле цикла перезаписывает внешнюю переменную n,
# тк циклы не создают новую область видимости переменных
for n in nums:
    print(n)  # Вывод: 1 2 3 4 5 6 7

print(n)  # Вывод: 7
print()
# Break
# В Python выражение break дает возможность выйти из цикла при условии.
for num in nums:
    if num == 4:
        print('Выход из цикла')
        break
    print(num),
print()
# Continue
# В Python выражение continue дает возможность пойти дальше по циклу при условии.
for num in nums:
    if num == 4:
        print('Пропускаем 4')
        continue
    print(num)
print()
for num in nums:
    if num == 3:
        print('Пропускаем 3')
        continue
    elif num == 5:
        print('Выход из цикла')
        break
    print(num)

print()
# pass
for num in nums:
    if num == 2:
        print('Ничего не делаем\nНе пропускаем 2 и не выходим из цикла')
        pass
    elif num == 3:
        print('Пропускаем 3')
        continue
    elif num == 5:
        print('Выход из цикла')
        break
    print(num)

# For ... else
# For может содержать блок else, который выполнится, только если цикл завершится полностью (без применения break)
print()
# Выведется надпись Конец цикла
for num in nums:
    if num == 2:
        print('Ничего не делаем\nНе пропускаем 2 и не выходим из цикла')
        pass
    elif num == 3:
        print('Пропускаем 3')
        continue
else:
    print('Конец цикла')

print()
# Не выведется надпись Конец цикла, потому что цикл был прерван конструкцией break
for num in nums:
    if num == 2:
        print('Ничего не делаем\nНе пропускаем 2 и не выходим из цикла')
        pass
    elif num == 3:
        print('Пропускаем 3')
        continue
    elif num == 5:
        print('Выход из цикла')
        break
else:
    print('Конец цикла')
