salario = 2030
aumento = 3

for i in range(1997, 2021):
    print(f"Ano: {i}")
    salario = salario + ((salario * aumento) / 100)
    aumento = aumento + 1.5

print(round(salario, 2))
