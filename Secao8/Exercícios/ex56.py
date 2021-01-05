import numpy as np


def funcao(m, linha):
    return sum(m[linha - 1, :])


n = int(input("Informe a linha: "))
matriz = np.array([x for x in range(42)]).reshape(7, 6)
print(matriz)
print(f"Linha selecionada[{n}]: {funcao(matriz, n)}")
