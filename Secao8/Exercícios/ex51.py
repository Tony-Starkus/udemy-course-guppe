import numpy as np


def funcao(x):
    aux = 0
    for i in range(3):
        for j in range(3):
            if i == 3 - 1 - j:
                aux = aux + x[i][j]


matriz = np.array([x for x in range(9)]).reshape(3, 3)
print(matriz)
funcao(matriz)
