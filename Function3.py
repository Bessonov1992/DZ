def spiski():
    print("Введите длинну 1 списка")
    a = int(input())
    print("Введите максимальное значение 1 списка")
    b = int(input())
    from random import randint
    list1 = [randint(1, b) for i in range(a)]
    print(list1)
    print("Введите длинну 2 списка")
    c = int(input())
    print("Введите максимальное значение 2 списка") # привет
    d = int(input())
    from random import randint
    list2 = [randint(1, d) for i in range(c)]
    print(list2)
    list3 = []
    for e in range(len(list1)):
        if list1[e] > list2[e]:
            list3.append(list1[e])
        else:
            list3.append(list2[e])
    print("числа с большим значением - ", list3)
spiski()