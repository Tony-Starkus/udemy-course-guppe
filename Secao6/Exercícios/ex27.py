num = int(input("Digite um número inteiro positivo: "))
valor = 0
if num < 0:
    print("O número não é positivo")
else:
    for i in range(1, num + 1):
        valor = valor + (1 / i)
    print(valor)
