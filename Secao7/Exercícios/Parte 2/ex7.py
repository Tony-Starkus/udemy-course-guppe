matriz = []

for i in range(10):
    row = []
    for j in range(10):
        if i < j:
            row.append((2*i) + (7*j) - 2)
        elif i == j:
            row.append((3*(i**2)) - 1)
        else:
            row.append((4*(i**3)) - (5*(j**2)))
    matriz.append(row)

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()
