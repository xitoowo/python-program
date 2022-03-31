class Strict:
    __slots__ = ('__init__', 'x', 'y', '__repr__')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Strict({self.x},{self.y})'


instance_1 = Strict(1, 1)
instance_2 = Strict(2, 2)

my_set = {instance_1, instance_2}
print(my_set)  # {Strict(1,1), Strict(2,2)}

my_dict = {instance_1: [1, 2, 3], instance_2: [4, 5, 6]}
print(my_dict)  # {Strict(1,1): [1, 2, 3], Strict(2,2): [4, 5, 6]}

instance_1.x = 3
print(my_set)  # {Strict(3,1), Strict(2,2)}
print(my_dict)  # {Strict(3,1): [1, 2, 3], Strict(2,2): [4, 5, 6]}

print(my_dict.get(instance_1))  # [1, 2, 3]
