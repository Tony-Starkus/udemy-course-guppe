print("Informe 10 números!")
valores = []

for i in range(10):
    num = float(input("Número: "))
    if num.is_integer():
        num = int(num)
    valores.append(num)
    valores.sort()
    print(valores)
