km = float(input("Informe a distância em Km: "))
consumo = float(input("Informe a quantidade de gasolina consumida em litros: "))
x = consumo / km

if x < 8:
    print("Venda o carro!")
elif x in range(8, 14):
    print("Econômico!")
