notas = list()

for i in range(4):
    notas.append(float(input("Digite uma nota: ")))

print(f"A média aritmética é: {sum(notas) / 4}")
