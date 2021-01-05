N = int(input("Informe a quantidade de números: "))
valores = {}

for i in range(N):
    x = float(input("Informe o valor: "))
    if x not in valores:
        valores.update({x: 1})
    else:
        valores[x] = valores[x] + 1

print(f"O maior número é {max(valores)} e ele foi digitado {valores[max(valores)]} vezes")
