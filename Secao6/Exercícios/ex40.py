valores = []
while True:
    num = int(input("Informe um número inteiro: "))
    if num < 0:
        break
    else:
        valores.append(num)

print(f"Maior valor: {max(valores)}")
print(f"Menor valor: {min(valores)}")
