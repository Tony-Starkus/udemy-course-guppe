matriz = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input("Informe um número inteiro: ")))
    matriz.append(row)

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()

valores = []
for index1, i in enumerate(matriz):
    for index2, j in enumerate(i):
        if index1 == index2:
            valores.append(j)

print(sum(valores))
