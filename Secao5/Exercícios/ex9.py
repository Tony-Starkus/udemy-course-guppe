salario = float(input("Digite o salário do trabalhador: "))
prestacao = float(input("Digite o valor da prestação: "))
x = (salario * 20) / 100
if x < prestacao:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
