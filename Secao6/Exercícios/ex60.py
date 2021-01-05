valores = []

while True:
    num = float(input("Informe um número: "))
    if num.is_integer():
        num = int(num)
    if num == 0:
        break
    else:
        valores.append(num)

print(f"a) Soma dos valores: {sum(valores)}")
print(f"b) {len(valores)} valores digitados")
print(f"c) Média: {sum(valores) / len(valores)}")
print(f"d) Maior número: {max(valores)}")
print(f"e) Menor número: {min(valores)}")
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print(f"f) Média dos pares: {sum(pares) / len(pares)}")
