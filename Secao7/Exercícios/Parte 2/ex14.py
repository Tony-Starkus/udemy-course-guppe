import random

matriz = []

for i in range(5):
    # row = list(random.sample(range(100), 5))
    row = [random.randint(0, 100) for _ in range(5)]
    matriz.append(row)

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()
