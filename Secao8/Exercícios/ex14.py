d = float(input("Informe a distância em Km: "))
lt = float(input("Informe o quantidade de litros de gasolina: "))

x = d / lt

if x < 8:
    print("Venda o carro!")
elif 8 <= x <= 14:
    print("Econômico!")
else:
    print("Super econômico!")
