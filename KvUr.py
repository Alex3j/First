a = int(input("Введите коэф. a, не равный 0  = "))
b = int(input("Введите коэф. b = "))
c = int(input("Введите коэф. с = "))

D = b**2-4*a*c
if D >= 0:
    x1 = (-b+D**0.5) / (2*a)
    x2 = (-b-D**0.5) / (2*a)
    if x1 == x2:
        print(x1)
    else:
        print(x1, x2)
else:
    print("Решений нет")