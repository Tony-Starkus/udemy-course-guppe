vetor1 = []
vetor2 = []
vetor3 = []

print("Vetor 1")
for i in range(10):
    num = float(input("Informe um número: "))
    if num.is_integer():
        num = int(num)

print("Vetor 2")
for i in range(10):
    num = float(input("Informe um número: "))
    if num.is_integer():
        num = int(num)

print("Vetor 3")
for x, y in zip(vetor1, vetor2):
    vetor3.append(x)
    vetor3.append(y)

print(vetor3)
