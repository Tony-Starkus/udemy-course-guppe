matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()

col_1 = []
col_2 = []
col_3 = []

for i in matriz:
    for index, j in enumerate(i):
        if index == 0:
            col_1.append(j)
        elif index == 1:
            col_2.append(j)
        else:
            col_3.append(j)

matriz_T = [col_1, col_2, col_3]
print("Transposta: ")
for i in matriz_T:
    for j in i:
        print(j, end=" ")
    print()
