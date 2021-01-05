valores = [0, 1, 1]
while valores[len(valores) - 1] + valores[len(valores) - 2] < 4000000:
    valores.append(valores[len(valores) - 1] + valores[len(valores) - 2])

print(valores)
