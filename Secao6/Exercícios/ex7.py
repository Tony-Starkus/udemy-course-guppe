valores = []
aux = 0
for i in range(10):
    valor = int(input("Digite um número inteiro: "))
    if valor >= 0:
        valores.append(valor)
        aux = aux + 1

print(sum(valores) / aux)
