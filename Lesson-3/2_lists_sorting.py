# Сортировка списков

# Сортировка методом sort() (без возврата значений, с текущим объектом)
# Этот метод берет список и сортирует его. На выходе мы получаем тот же список, только отсортированный.
mylist = [99, 0, 25, 8, 4]
mylist.sort()
print(mylist)  # [0, 4, 8, 25, 99]

# Метод sort() может принимать два необязательных аргумента: key и reverse.
# Значением key выступает функция, которая будет вызываться для каждого элемента в списке.
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
print(names)  # ['Jessica', 'Ben', 'Carl', 'Jackie', 'Wendy']
# Таким образом, key=len укажет отсортировать список по длине имен, от наименьшего к наибольшему.
names.sort(key=len)
print(names)  # ['Ben', 'Carl', 'Wendy', 'Jackie', 'Jessica']
# reverse - вернуть отсортированный список в обратном порядке
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
print(names)  # ['Jessica', 'Ben', 'Carl', 'Jackie', 'Wendy']
names.sort(key=len, reverse=True)
print(names)  # ['Jessica', 'Jackie', 'Wendy', 'Carl', 'Ben']

# Сортировка функцией sorted() (с возвратом значений, создание нового объекта)
# sorted() принимает любые итерируемые объекты(списки, строки, кортежи и т.д.),
# тогда как метод sort() работает только со списками.
mylist = [99, 0, 25, 8, 4]
mylist_sorted = sorted(mylist)
print(mylist)  # [99, 0, 25, 8, 4]
print(mylist_sorted)  # [0, 4, 8, 25, 99]

# sorted() тоже может принимать два необязательных аргумента: key и reverse.
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
names_sorted = sorted(names, key=len)
print(names_sorted)  # ['Ben', 'Carl', 'Wendy', 'Jackie', 'Jessica']
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
names_sorted = sorted(names, key=len, reverse=True)
print(names_sorted)  # ['Jessica', 'Jackie', 'Wendy', 'Carl', 'Ben']

# sorted() создает новый объект, независимый от старого
mylist_1 = [4, 9, 8, 6]
mylist_2 = sorted(mylist_1)
mylist_1[0] = 1
mylist_2[0] = 2
print(mylist_1)  # [1, 9, 8, 6]
print(mylist_2)  # [2, 6, 8, 9]
