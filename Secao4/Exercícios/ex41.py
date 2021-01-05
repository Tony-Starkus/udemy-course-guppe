valor = float(input("Digite o valor da hora de trabalho: "))
horas = float(input("Digite o número de horas trabalhados: "))
x = ((valor * horas) * 10) / 100
print(f"O valor a ser pago é: {valor + x}")
