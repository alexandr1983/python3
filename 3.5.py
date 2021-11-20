def summa(*args):
    s = 0
    flag = False
    for i in args:
        try:
            if i:
                s += int(i)
        except ValueError:
            flag = True
    return s, flag

sum = 0

while True:
    n = input('Vvedite chisla cherez probel: ').split(' ')
    s, flag = summa(*n)
    sum += s
    print(f"Summa: {sum}")
    if flag:
        break
