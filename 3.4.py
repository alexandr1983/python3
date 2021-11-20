def my_func(x, y):
    print(x ** y)


def my_func2(x, y):
    k = x
    for i in range(1, y):
        k = k * x
    print(k)



print("Variant 1: ")
my_func(int(input("Enter Х: ")), int(input("Enter Y: ")))
print("Variant 2: ")
my_func2(int(input("Enter Х: ")), int(input("Enter Y: ")))
