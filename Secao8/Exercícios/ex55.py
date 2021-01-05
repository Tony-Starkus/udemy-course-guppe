import numpy as np


def funcao(x):
    principal = 0
    secundaria = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                principal = principal + x[i][j]
            elif i == 3 - 1 - j:
                secundaria = secundaria + x[i][j]
    return {"principal": principal, "secundaria": secundaria}


matriz = np.array([x for x in range(9)]).reshape(3, 3)
print(funcao(matriz))
