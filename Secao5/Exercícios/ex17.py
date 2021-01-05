bM = float(input("Digite o valor da base maior: "))
bm = float(input("Digite o valor da base menor: "))
h = float(input("Digite o valor da altura: "))

if bM <= 0 or bm <= 0:
    print("O valor das bases não pode ser 0")
else:
    A = ((bM + bm) * h) / 2
    print(f"A área do trapézio é: {round(A, 2)}")
