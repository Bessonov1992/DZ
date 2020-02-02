def spisok():
    print("Введите длинну списка")
    a = int(input())
    print("Введите максимальное значение списка")
    b = int(input())
    from random import randint
    list = [randint(1, b) for i in range(a)]
    print(list)
spisok()
