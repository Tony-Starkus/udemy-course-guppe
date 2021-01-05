import numpy as np


def funcao(x):
    new = np.array([x[:, i] for i in range(n)]).reshape(n, n)
    print(new)


n = int(input("Informe N para o tamanho da matriz quadrada: "))
matriz = np.array([x for x in range(1, n * n + 1)]).reshape(n, n)
funcao(matriz)
