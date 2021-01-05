vetor1 = []
for i in range(10):
    vetor1.append(float(input("Digite um número: ")))
vetor2 = []
for i in range(10):
    vetor2.append(float(input("Digite um número: ")))

print(set(vetor1 + vetor2))
