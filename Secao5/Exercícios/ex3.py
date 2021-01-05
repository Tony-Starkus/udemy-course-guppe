from math import pow, sqrt

num = float(input("Digite um número real: "))

if num >= 0:
    print(f"A raiz quadrada desse número é: {sqrt(num)}")
else:
    print(f"O número ao quadrado é: {pow(num, 2)}")
