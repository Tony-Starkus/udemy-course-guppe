from math import pow, sqrt

num = float(input("Digite um número: "))

if num >= 0:
    print(f"O número ao quadrado é: {pow(num, 2)}")
    print(f"A raiz quadrada do número é: {sqrt(num)}")
else:
    print("O número é negativo")
