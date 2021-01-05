valores = ()
for i in range(10):
    x = float(input("Digite um valor: "))
    valores = valores + (x, )

aux = sum(valores)
print(f"Somatório: {aux}")
