import numpy as np


def soma(x):
    aux = 0
    for i in range(4):
        for j in range(4):
            aux = aux + x[i][j]
    return aux


matriz = np.array([x for x in range(16)]).reshape(4, 4)
print(matriz)
print(soma(matriz))
