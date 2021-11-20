def delenie(a, b):
    if b != 0:
        c = a / b
        print(f"a / b = {c}")
    else:
        print('na 0 ne delyat')



a = int(input("Vvedite a: "))
b = int(input("Vvedite b: "))
delenie(a, b)
