matriz1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matriz2 = [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
matriz3 = []

for i in range(4):
    matriz3.append(max(matriz1[i] + matriz2[i]))

print(matriz3)
