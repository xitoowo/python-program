with open('little_dorrit_1', 'r', encoding='utf-8') as file:
    counter = 1
    for row in file:
        if counter <= 10:
            print(row, end='')
            counter += 1
