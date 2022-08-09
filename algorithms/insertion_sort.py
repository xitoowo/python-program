my_list = [10, 5, 13, 8, 2]

for i in range(1, len(my_list)):
    value = my_list[i]  # На первой итерации 5
    j = i - 1  # 0
    while j >= 0 and my_list[j] > value:  # пока 0 >= 0 and 10 > 5
    # while j >= 0 and my_list[j] > value:  # [2, 5, 8, 10, 13]
    # while j >= 0 and my_list[j] < value:  # [13, 10, 8, 5, 2]
        my_list[j + 1] = my_list[j]  # my_list[10] = my_list[10]
        j -= 1  # -1
        # print(j)
    print(j)
    my_list[j + 1] = value  # my_list[10] = 5
    # print(my_list[j + 1])

print(my_list)  # [2, 5, 8, 10, 13]
