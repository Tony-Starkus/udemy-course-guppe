vetor = [1, 2, 3]

for i in range(10):
    vetor.append(int(input("Informe um número inteiro: ")))

print(vetor)
print(f"Maior elemento: {max(vetor)} | Posição: {vetor.index(max(vetor))}")
