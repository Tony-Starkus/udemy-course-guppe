vetor = []
for i in range(10):
    vetor.append(int(input("Informe um número inteiro: ")))

vetor1 = []
vetor2 = []

for num in vetor:
    if num % 2 == 0:
        vetor2.append(num)
    else:
        vetor1.append(num)

print(f"V1: {vetor1}")
print(f"V2: {vetor2}")
