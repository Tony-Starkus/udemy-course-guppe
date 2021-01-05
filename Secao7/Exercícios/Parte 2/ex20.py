import numpy as np
from random import random

matriz = np.array([random() * 100 for _ in range(18)])
matriz = matriz.reshape(3, 6)
a = []
b = []

aux1 = []
aux2 = []
for index_row, row in enumerate(matriz):
    for index_col, col in enumerate(row):
        if index_col == 0:
            aux1.append(col)
        if index_col == 1:
            aux2.append(col)
        if index_col % 2 == 1:
            a.append(col)
        if index_col == 1 or index_col == 3:
            b.append(col)

print(matriz)
matriz = np.delete(matriz, 5, 1)
c = np.array([x + y for x, y in zip(aux1, aux2)]).reshape(3, 1)
print()
matriz = np.append(matriz, c, axis=1)
print(matriz)

