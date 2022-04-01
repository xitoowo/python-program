with open('comments_taget.py', 'r') as reader:
    for line in reader:
        if line.startswith('#'):
            continue
        print(line, end='')

