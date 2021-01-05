vetor = []
for i in range(10):
    vetor.append(int(input("Informe um número inteiro: ")))

for i in range(len(vetor)):
    if vetor[i] == 1:
        continue
    primo = True
    for j in range(i - 1, 1, -1):
        if vetor[i] % j == 0:
            primo = False
            break
    if primo:
        print(f"Número: {vetor[i]} | Posição: {i}")
