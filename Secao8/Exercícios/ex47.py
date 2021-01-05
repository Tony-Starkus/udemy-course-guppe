import numpy as np


def funcao(x):
    aux = 0
    for i in x:
        for j in i:
            if j > 10:
                aux = aux + 1
    print(aux)


matriz = np.array([x for x in range(16)]).reshape(4, 4)
funcao(matriz)
