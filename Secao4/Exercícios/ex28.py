valores = []
for i in range(3):
    numero = float(input("Digite um número: "))
    valores.append(numero ** 2)

print(f"A soma dos três valores é: {sum(valores)}")
