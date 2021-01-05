valor = float(input("Digite o valor da venda: "))

if valor < 20000:
    comissao = (valor * 14) / 100
    print(f"Comissão do vendedor: {400 + comissao}")
elif 20000 >= valor < 40000:
    comissao = (valor * 14) / 100
    print(f"Comissão do vendedor: {500 + comissao}")
elif 40000 >= valor < 60000:
    comissao = (valor * 14) / 100
    print(f"Comissão do vendedor: {550 + comissao}")
elif 60000 >= valor < 80000:
    comissao = (valor * 14) / 100
    print(f"Comissão do vendedor: {600 + comissao}")
elif 80000 >= valor < 100000:
    comissao = (valor * 14) / 100
    print(f"Comissão do vendedor: {650 + comissao}")
else:
    comissao = (valor * 16) / 100
    print(f"Comissão do vendedor: {700 + comissao}")
