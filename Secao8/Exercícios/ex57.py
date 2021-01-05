import numpy as np


def funcao(m, coluna):
    return sum(m[:, coluna - 1])


n = int(input("Informe a coluna: "))
matriz = np.array([x for x in range(42)]).reshape(7, 6)
print(matriz)
print(f"Coluna selecionada[{n}]: {funcao(matriz, n)}")

