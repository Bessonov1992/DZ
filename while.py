print("ВВедите значение А")
a = int(input())
print("Введите значение B")
b = int(input())
print("Введите значение С")
c = int(input())
while a < b:
    print(a)
    print("Пока что нет")
    a = a + c
if a > b:
    print(a)
    print("Дождались!")
else:
    print("а равно б")