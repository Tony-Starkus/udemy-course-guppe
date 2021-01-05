altura = float(input("Digite a altura da pessoa: "))
peso = float(input("Digite o peso da pessoa: "))

if altura < 1.20:
    if peso <= 60:
        print("A")
    elif peso in range(60, 91):
        print("D")
    elif peso > 90:
        print("G")
elif 1.20 <= altura <= 1.70:
    if peso <= 60:
        print("B")
    elif 60 < peso <= 90:
        print("E")
    elif peso > 90:
        print("H")
elif altura > 1.70:
    if peso <= 60:
        print("C")
    elif peso < 60 and peso <= 90:
        print("F")
    elif peso > 90:
        print("I")
