from math import sqrt

a = float(input("Informe o valor de a: "))
if a.is_integer():
    a = int(a)

b = float(input("Informe o valor de b: "))
if b.is_integer():
    b = int(b)

x = sqrt((a**2) + (b**2))
if x.is_integer():
    x = int(x)

if isinstance(x, int):
    print(x)
else:
    print("Não é terno pitagórico")
