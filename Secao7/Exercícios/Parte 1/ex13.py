vetor = []

for i in range(5):
    vetor.append(float(input("Informe um valor: ")))

print(f"Posição do maior: {vetor.index(max(vetor))}")
print(f"Posição do menor: {vetor.index(min(vetor))}")
