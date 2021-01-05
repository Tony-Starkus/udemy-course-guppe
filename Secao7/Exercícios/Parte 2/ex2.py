matriz = []

for i in range(5):
    row = []
    for j in range(5):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    matriz.append(row)

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()
