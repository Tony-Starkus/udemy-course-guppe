import numpy as np


def produto_matricial(a, b):
    return np.matmul(a, b)


matriz1 = np.array([x for x in range(16)]).reshape(4, 4)
matriz2 = np.array([x for x in range(16, 32)]).reshape(4, 4)
print(matriz1)
print(matriz2)
print(produto_matricial(matriz1, matriz2))
