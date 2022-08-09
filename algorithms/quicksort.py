def quicksort(array: list):
    if len(array) < 2:  # если длина 1 и меньше
        return array
    pivot = array[0]  # опорный элемент
    less = [i for i in array[1:] if i <= pivot]  # от 1 потому что опорный это первый элемент (0 индекс)
    greater = [i for i in array[1:] if i > pivot]
    print(less, greater)
    return quicksort(less) + [pivot] + quicksort(greater)


data = [10, 5, 6, 9, 1, 0]
result = quicksort(data)
print(data is result)
