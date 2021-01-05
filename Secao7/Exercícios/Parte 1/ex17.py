vetor = []

for i in range(10):
    vetor.append(float(input("Informe um número: ")))

print(vetor)
for i in range(10):
    if vetor[i] < 0:
        vetor[i] = 0

print(vetor)
