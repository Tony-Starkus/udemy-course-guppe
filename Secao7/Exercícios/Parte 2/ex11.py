matriz = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
aux = []
for index1, i in enumerate(matriz):
    for index2, j in enumerate(i):
        print(j, end=" ")
        if index1 + index2 == (len(matriz) - 1):
            aux.append(j)
    print()

print(aux)
print(sum(aux))
