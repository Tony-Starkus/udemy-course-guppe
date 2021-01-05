
while True:
    op = int(input("1. Converter km/h para m/s\n2. Converter m/s para km/h\n0. Finalizar\nOpção: "))
    if op == 0:
        break
    elif op == 1:
        x = float(input("Informe o valor em km/h: "))
        if x.is_integer():
            x = int(x)
        print(f"{x / 3.6} m/s")
    elif op == 2:
        x = float(input("Informe o valor em m/s: "))
        if x.is_integer():
            x = int(x)
        print(f"{x * 3.6} m/s")
    else:
        print("Operação Inválida")
