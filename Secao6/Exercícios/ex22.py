valores = []

while True:
    nota = int(input("Informe a nota: "))
    if nota in range(10, 21):
        valores.append(nota)
    else:
        break

print(f"A média é: {sum(valores) / len(valores)}")
