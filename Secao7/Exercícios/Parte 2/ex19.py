import numpy as np
"""
arr = np.arange(15)
print(arr)
print(arr.reshape(3, 5))

"""
matriz = []
for i in range(5):
    matriz = np.concatenate(
        (matriz, [float(x) for x in list(input("Informe os valores separados por espaço: ").split(" "))])
    )
matriz = matriz.reshape(5, 3)

notas_finais = []
maior_nota = []
for row in matriz:
    aux = 0
    for j in row[1:]:
        aux = aux + j
    notas_finais.append(aux)
    maior_nota = [notas_finais.index(max(notas_finais)), max(notas_finais)]

matriz = np.insert(matriz, 3, notas_finais, axis=1)
print(f"Maior nota: {maior_nota}")
print(f"Média notas finais: {sum(notas_finais) / len(notas_finais)}")

