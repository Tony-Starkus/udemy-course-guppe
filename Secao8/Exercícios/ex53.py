import numpy as np


def funcao(x):
    identidade = True
    for i in range(n):
        for j in range(n):
            if i == j:
                if x[i][j] != 1:
                    identidade = False
                    break
            else:
                if x[i][j] != 0:
                    identidade = False
                    break
    return identidade


n = int(input("Informe N para o tamanho da matriz quadrada: "))
matriz_identidade = np.identity(n)
print(funcao(matriz_identidade))
