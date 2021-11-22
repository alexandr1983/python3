def int_func(a):
    k = a.split(' ')
    b = []
    for i in k:
        el = str(i)
        zagl = el[:1].upper()
        c = zagl + el[1:]
        b.append(c)
    return b



print(int_func(input()))
