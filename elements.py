def elemsum():
    a = ''.join(input())
    b = list(a)
    c = 0
    for i in b:
        c += int(i)
    print(c)
elemsum()