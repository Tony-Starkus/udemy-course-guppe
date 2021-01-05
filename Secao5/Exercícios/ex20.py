A = float(input("Digite o primeiro valor: "))
B = float(input("Digite o segundo valor: "))
C = float(input("Digite o terceiro valor: "))

if A < B + C and B < A + C and C < B + A:
    if A == B == C:
        print("O triângulo é um quadrilátero")
    elif A == B or A == C or C == B:
        print("O triângulo é um isósceles")
    elif A != B != C:
        print("O triângulo é um escaleno")
else:
    print("O valores não formam um triângulo!")
