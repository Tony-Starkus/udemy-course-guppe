from random import randrange

matriz = [list(randrange(0, 11) for _ in range(10)) for _ in range(3)]

for row in matriz:
    for item in row:
        print(item, end=" ")
    print()

for row in matriz:
    pior = {}
    menor = min(row)
    for index, item in enumerate(row):
        if item == menor:
            pior.update({index: item})
            break
    print(pior)
