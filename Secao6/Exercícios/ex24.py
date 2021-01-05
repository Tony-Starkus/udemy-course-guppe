num = int(input("Digite um número inteiro: "))
valores = []
for i in range(1, num + 1):
    if i == num:
        break
    elif num % i == 0:
        valores.append(i)

print(f"A soma dos divisores é: {sum(valores)}")
