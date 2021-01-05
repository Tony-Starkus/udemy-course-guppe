from math import log
num = int(input("Digite um número inteiro: "))
if num < 0:
    print(f"Número inválido")
else:
    print(f"O logaritmo deste número é: {log(num)}")
