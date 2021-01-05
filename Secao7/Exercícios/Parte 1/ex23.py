vetor1 = []
vetor2 = []

for i in range(5):
    num = input("Informe dois números, separados por espaço: ").split()
    vetor1.append(float(num[0]))
    vetor2.append(float(num[1]))

res = 0
for x, y in zip(vetor1, vetor2):
    res = res + (x * y)

print(res)
