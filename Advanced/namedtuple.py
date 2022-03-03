# Именованные кортежи — это легковесные объекты.
# Их преимущество заключается в том, что создавать их очень просто.
# Для этого потребуется встроенная функция, доступная в модуле Collections.
#
# Если вам нужен класс для управления данными — рассмотрите в качестве альтернативы именованные кортежи.
from collections import namedtuple
Product = namedtuple('Product', 'name price')
milk = Product('Молоко', 65.5)
print(milk)
print(milk.name)
print(milk.price)
