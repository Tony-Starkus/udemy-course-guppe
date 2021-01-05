from math import sqrt
while True:
    num = float(input("Digite um valor: "))
    if num < 0:
        break
    if num.is_integer():
        num = int(num)

    print(f"{num}² = {num**2}")
    print(f"{num}³ = {num**3}")
    print(f"sqrt({num}) = {sqrt(num)}")
