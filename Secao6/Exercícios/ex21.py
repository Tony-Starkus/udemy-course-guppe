num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

soma_pares = 0
multi_impares = 1
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma_pares = soma_pares + i
    else:
        multi_impares = multi_impares * i


print(f"A soma dos pares é: {soma_pares}")
print(f"A multiplicação dos impares é: {multi_impares}")
