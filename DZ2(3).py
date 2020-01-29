from random import randint
a = [randint(0, 100) for i in range(10)]
del a [-1]
print(a)
