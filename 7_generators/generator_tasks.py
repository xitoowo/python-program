from random import randint


# Генератор ip
def ip_generator():
    for _ in range(10):
        data = [randint(0, 255) for x in range(4)]
        ip = "{}.{}.{}.{}".format(*data)
        yield ip


for index, i in enumerate(ip_generator(), start=1):
    print(index, i)


# Программа на Python для генерации степеней 2
# от 2 до 256
def get_next_num():
    n = 2

    # Бесконечный цикл для генерации степеней 2
    while True:
        yield n
        n *= 2  # При последующем обращении к
        # get_next_num() выполнение
        # продолжится отсюда


# Код для проверки get_next_num()
for num in get_next_num():
    if num > 256:
        break
    print(num)
