vetor1 = []
for i in range(10):
    vetor1.append(float(input("Digite um número: ")))
vetor2 = []
for i in range(10):
    vetor2.append(float(input("Digite um número: ")))

print(set(x for x in vetor1 if x in vetor1 and x in vetor2))
