from math import sqrt

num = float(input("Digite um número: "))

if num >= 0:
    print(f"A raiz quadrada desse número é: {sqrt(num)}")
else:
    print("O número é inválido!")
