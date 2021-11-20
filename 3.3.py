def my_func(a, b, c):
    k = min(a, b, c)
    print(f"Summa naibolshih: {a + b + c - k}")


my_func(int(input("Vvedite a: ")), int(input("Vvedite b: ")), int(input("Vvedite a: ")))
