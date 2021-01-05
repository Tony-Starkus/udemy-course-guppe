custo = float(input("Informe o custo de fábrica: "))

if custo <= 12000:
    distribuidor = (custo * 5) / 100
    print(f"Custo ao consumidor: {custo + distribuidor}")
elif 12000 >= custo <= 25000:
    distribuidor = (custo * 10) / 100
    impostos = (custo * 15) / 100
    print(f"Custo ao consumidor: {custo + distribuidor + impostos}")
elif custo >= 25000:
    distribuidor = (custo * 15) / 100
    impostos = (custo * 20) / 20
    print(f"Custo ao consumidor: {custo + distribuidor + impostos}")
