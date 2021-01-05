matriz = []
for i in range(5):
    row = []
    for j in range(5):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    matriz.append(row)

num = int(input("Qual valor deseja encontrar?: "))

for i in matriz:
    for j in i:
        if j == num:
            print(matriz.index(i), i.index(j))
            exit()

print("Não encontrado!")
