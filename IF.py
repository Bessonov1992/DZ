print("ВВедите значение А")
a =int(input())
print("Введите значение B")
b = int(input())
print("Введите значение С")
c = int(input())
if a > b:
    print("Свершилось!")
if b > a:
    print("Да ну!")
if a == b:
    print("А если так?")
    a = a + c
    b = b - c
    if a > b:
        print("Свершилось!")
    if b > a:
        print("Да ну!")