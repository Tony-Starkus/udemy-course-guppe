valores = []
while True:
    num = int(input("Digite a idade: "))
    if num < 1:
        break
    else:
        valores.append(num)

print(f"Idade média: {sum(valores) / len(valores)}")
