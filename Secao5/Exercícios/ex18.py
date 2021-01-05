op = int(input("Escola a operação: \n(1) Adição\n(2) Subtração\n(3) Multiplicação\n(4) Divisão\n: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if op == 1:
    print(f"Resultado: {num1 + num2}")
elif op == 2:
    print(f"Resultado: {num1 - num2}")
elif op == 3:
    print(f"Resultado: {num1 * num2}")
elif op == 4:
    print(f"Resultado: {num1 / num2}")
else:
    print("Operação inválida")
