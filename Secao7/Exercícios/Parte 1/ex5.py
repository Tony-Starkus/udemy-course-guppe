vetor = []
pares = 0
for i in range(10):
    num = float(input("Digite um número: "))
    if num.is_integer():
        num = int(num)
    if num % 2 == 0:
        pares = pares + 1
    vetor.append(num)

print(vetor)
print(f"Total pares: {pares}")
