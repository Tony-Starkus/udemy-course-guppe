from random import randint

matriz = [list(randint(-10, 10) for _ in range(3)) for _ in range(3)]

for row in matriz:
    for i in row:
        print(i, end=" ")
    print()

col1 = []
col2 = []
col3 = []
for row in matriz:
    for index, j in enumerate(row):
        if index == 0:
            col1.append(j)
        elif index == 1:
            col2.append(j)
        else:
            col3.append(j)

print([sum(col1), sum(col2), sum(col3)])
