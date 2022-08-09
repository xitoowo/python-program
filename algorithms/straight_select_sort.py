# Сортировка выбором
# Суть сортировки
# В неотсортированном подмассиве (for j in range(i + 1, len(my_list))) ищется локальный максимум (минимум).
# Найденный максимум (минимум) меняется местами с последним (первым) элементом в подмассиве.

my_list = [4, 6, 5, 9, 11]

for i in range(0, len(my_list) - 1):
    min_value = i  # запоминаем индекс элемента
    for j in range(i + 1, len(my_list)):
        if my_list[j] < my_list[min_value]:
            min_value = j
    my_list[i], my_list[min_value] = my_list[min_value], my_list[i]


print(my_list)