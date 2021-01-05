vetor = []
valores_iguais = []

for i in range(10):
    num = float(input("Informe um número: "))
    if num in vetor:
        if num not in valores_iguais:
            valores_iguais.append(num)

    vetor.append(num)

print(vetor)
print(valores_iguais)
