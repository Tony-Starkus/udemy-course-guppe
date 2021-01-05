valores = [1, 2, 4, 50, 39, 20, 29, 39, 49, 103, 40439, 30539, 303293, 1000, 100]
pares = 0
for valor in valores:
    if valor == 1000:
        break
    elif valor % 2 == 0:
        pares = pares + 1

print(f"Total de pares: {pares}")
