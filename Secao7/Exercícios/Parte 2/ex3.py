matriz = []

for i in range(4):
    row = []
    for j in range(4):
        row.append(i * j)
    matriz.append(row)

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()
