a = float(input("Введіть довжину 1ої сторони трикутника: "))
b = float(input("Введіть довжину 2ої сторони трикутника: "))
c = float(input("Введіть довжину 3ої сторони трикутника: "))
if a == 0 or b == 0 or c == 0:
    print("Таких трикутників немає")
else:
    p = a + b + c
    if p > 20:
        print("найбільша сторона:", max(a, b, c))
    elif p < 10:
        print("найменша сторона:", min(a, b, c))
