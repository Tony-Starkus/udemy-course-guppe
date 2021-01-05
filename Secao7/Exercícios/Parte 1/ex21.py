A = []
B = []

print("vetor A")
for i in range(10):
    A.append(int(input("Informe um número inteiro: ")))

print("vetor B")
for i in range(10):
    B.append(int(input("Informe um número inteiro: ")))

print([x + y for x, y in zip(A, B)])
