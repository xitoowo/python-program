# Строки
# Одинарные и двойные кавычки равны между собой
my_string_o = 'Hello, World!'
my_string_d = "Hello, World!"
# Вывод: Hello, World!
print(my_string_o)
# Вывод: Hello, World!
print(my_string_d)

# Тройные кавычки сохраняют форматирование
my_string_to = '''      Hello, World!'''
my_string_td = """
    Hello, World!"""
# Вывод:       Hello, World!
print(my_string_to)
# Вывод: ----------
print('-' * 10)  # Напечатать символ 10 раз
# Вывод:
#     Hello, World!
print(my_string_td)

# Форматирование без тройных кавычек
my_string_of = "\t\tHello, World!"  # Повторение форматирования на строчке 9
# Вывод: 		Hello, World!
print(my_string_of)
# Вывод: ----------
print('-' * 10)  # Напечатать символ 10 раз
my_string_df = "\n\tHello, World!"  # Повторение форматирования на строчке 10
# Вывод:
# 	Hello, World!
print(my_string_df)

# Использование кавычек внутри строки
# Можно использовать одинарные кавычки внутри двойных и наоборот
# Вывод: "Hello, World!"
print('"Hello, World!"')
# Вывод: 'Hello, World!'
print("'Hello, World!'")
# Либо использовать экранирование \
# Вывод: 'Hello, World!'
print('\'Hello, World!\'')

# Операции над строками
# Вывод: HelloWorld
print('Hello' + 'World')
# Вывод: HelloHelloHelloWorldWorld
print('Hello' * 3 + 'World' * 2)
