n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

if n1 not in range(0, 11):
    print("A n1 não é válida")
if n2 not in range(0, 11):
    print("A n2 não é válida")

print(f"A média é: {round(((n1 + n2) / 2), 2)}")
