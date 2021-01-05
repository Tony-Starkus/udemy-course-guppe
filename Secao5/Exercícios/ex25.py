from math import pow, sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a <= 0:
    print("Não é equação do segundo grau!")
    exit()

delta = pow(-b, 2) - (4 * a * c)

if delta < 0:
    print("Não existe raiz")
elif delta == 0:
    print("Raiz única")
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
