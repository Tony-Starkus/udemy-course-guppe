b = float(input("Informe o valor da base: "))
if b < 1:
    print("O valor não pode ser menor que zero!")
    exit()
if b.is_integer():
    b = int(b)

h = float(input("Informe o valor da altura: "))
if h < 1:
    print("O valor não pode ser menor que zero!")
    exit()
if h.is_integer():
    h = int(h)

print((b * h) / 2)
