sal_carlos = float(input("Informe o salário de Carlos: "))
sal_joao = sal_carlos / 3

mes = 0
valor_carlos = sal_carlos
valor_joao = sal_joao

while valor_joao <= valor_carlos:
    mes = mes + 1
    valor_carlos = valor_carlos + ((valor_carlos * 2) / 100) + sal_carlos
    valor_joao = valor_joao + ((valor_joao * 5) / 100) + sal_joao

print(mes)
