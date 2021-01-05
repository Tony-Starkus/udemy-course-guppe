matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for index_col, i in enumerate(matriz):
    for index_row, j in enumerate(i):
        if index_row > index_col:
            i[index_row] = 0

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()
