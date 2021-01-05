uf = input("Escolha um estado [mg, sp, rj, ms]: ")
if uf.lower() not in ("mg", "sp", "rj", "ms"):
    print("Estado inválido")
    exit()

valor = float(input("Digite o valor do produto: "))
if uf.lower() == "mg":
    print(f"Preço final: R$ {valor + ((valor * 7) / 100)}")
elif uf.lower() == "sp":
    print(f"Preço final: R$ {valor + ((valor * 12) / 100)}")
elif uf.lower() == "rj":
    print(f"Preço final: R$ {valor + ((valor * 15) / 100)}")
else:
    print(f"Preço final: R$ {valor + ((valor * 8) / 100)}")
