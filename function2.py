def spisok():
    print("Введите длинну списка")
    a = int(input())
    print("Введите максимальное значение списка")
    b = int(input())
    from random import randint
    c = [randint(1, b) for i in range(a)]
    print(c)
    d = [e for e in c if e > 7]
    print("Больше 7", d)
spisok()