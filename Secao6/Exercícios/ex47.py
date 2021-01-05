while True:
    op = int(input("1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair\nOpção: "))
    if op == 5:
        break
    if op not in [1, 2, 3, 4]:
        print("Operação Inválida")
        continue

    num1 = float(input("Informe o primeiro valor: "))
    num2 = float(input("Informe o segundo valor: "))
    if num1.is_integer():
        num1 = int(num1)
    if num2.is_integer():
        num2 = int(num2)

    if op == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == 3:
        print(f"{num1} x {num2} = {num1 * num2}")
    elif op == 4:
        print(f"{num1} ÷ {num2} = {num1 / num2}")


