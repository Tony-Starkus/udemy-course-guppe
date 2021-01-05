print("Escolha uma opção:")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")
op = int(input("Opção: "))

if op not in range(1, 4):
    print("Operação inválida")
else:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if op == 1:
        print(f"{num1} + {num2}: {num1 + num2}")
    elif op == 2:
        if num1 == num2:
            raise Exception("Os números são iguais")
        else:
            print(f"{max(num1, num2)} - {min(num1, num2)} = {max(num1, num2) - min(num1, num2)}")
    elif op == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif op == 4:
        if num2 == 0:
            raise Exception("O denominador é zero!")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")

