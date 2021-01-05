valores_entrada = input("Digite 10 valores separados por espaço: ").split(" ")
valores = []
for valor in valores_entrada:
    valores.append(float(valor))

if len(valores) != 10:
    print("Você não digitou 10 valores!")
    exit()

print(sum(valores) / 10)
