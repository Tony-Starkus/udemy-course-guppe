salario = float(input("Informe o salário: "))
tempo = int(input("Informe o tempo de serviço em anos: "))

if salario <= 500:
    reajuste = (500 * 25) / 100
    salario = salario + reajuste
    if tempo in range(1, 4):
        salario = salario + 100
    elif tempo in range(4, 7):
        salario = salario + 200
    elif tempo in range(7, 11):
        salario = salario + 300
    else:
        salario = salario + 500
    print(salario)
elif 500 >= salario <= 1000:
    reajuste = (500 * 20) / 100
    salario = salario + reajuste
    if tempo in range(1, 4):
        salario = salario + 100
    elif tempo in range(4, 7):
        salario = salario + 200
    elif tempo in range(7, 11):
        salario = salario + 300
    else:
        salario = salario + 500
    print(salario)
elif 1000 >= salario <= 1500:
    reajuste = (500 * 15) / 100
    salario = salario + reajuste
    if tempo in range(1, 4):
        salario = salario + 100
    elif tempo in range(4, 7):
        salario = salario + 200
    elif tempo in range(7, 11):
        salario = salario + 300
    else:
        salario = salario + 500
    print(salario)
elif 1500 >= salario <= 2000:
    reajuste = (500 * 10) / 100
    salario = salario + reajuste
    if tempo in range(1, 4):
        salario = salario + 100
    elif tempo in range(4, 7):
        salario = salario + 200
    elif tempo in range(7, 11):
        salario = salario + 300
    else:
        salario = salario + 500
    print(salario)
elif salario > 2000:
    if tempo in range(1, 4):
        salario = salario + 100
    elif tempo in range(4, 7):
        salario = salario + 200
    elif tempo in range(7, 11):
        salario = salario + 300
    else:
        salario = salario + 500
    print(salario)
