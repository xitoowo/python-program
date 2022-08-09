# Ввод данных с клавиатуры
# Данные возвращаются в строковом формате
# Функция input позволяет вывод сообщения без вызова функции print

name = input("Name?\n")
print("Hello", name)
print("Hello " + name)
print(f"Hello {name}")
print("Hello {}".format(name))
print("Hello %s" % name)

# Функция type позволяет узнать тип переменной (имени)
# <class 'str'>
print(type(name))
