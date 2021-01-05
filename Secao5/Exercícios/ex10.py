h = float(input("Digite a altura: "))
s = input("Informe o sexo (M/F): ")

if s.lower() == "m":
    print(f"O peso ideal é: {(72.7 * h) - 58}")
elif s.lower() == "f":
    print(f"O peso ideal é: {(62.1 * h) - 44.7}")
else:
    print("O sexo informado é inválido")
