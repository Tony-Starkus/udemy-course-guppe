import numpy as np


def funcao(x):
    aux = 0
    for i in range(3):
        for j in range(3):
            if j < i:
                aux = aux + x[i][j]
    return aux


matriz = np.array([x for x in range(9)]).reshape(3, 3)
print(matriz)
print(funcao(matriz))
