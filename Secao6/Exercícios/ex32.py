from random import randrange
x = int(input("Informe o número de lançamentos: "))

for i in range(x + 1):
    d1 = randrange(1, 7)
    d2 = randrange(1, 7)
    if d1 > d2:
        print(f"{i}: d1[{d1}] > d2[{d2}]")
    elif d2 > d1:
        print(f"{i}: d2[{d2}] > d1[{d1}]")
    else:
        print(f"{i}: d1[{d1}] = d2[{d2}]")
