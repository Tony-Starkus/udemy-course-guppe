peso = float(input("Informe o peso emm kg: "))
altura = float(input("Informe a altura em metros: "))

IMC = peso / (altura ** 2)
IMC = round(IMC, 1)

if IMC <= 18.5:
    print("Abaixo do Peso")
elif 18.5 >= IMC <= 24.9:
    print("Saudável")
elif 25 <= IMC <= 29.9:
    print("Peso em excesso")
elif 30 <= IMC <= 34.9:
    print("Obesidade Grau 1")
elif 35 <= IMC <= 39.0:
    print("Obesidade Grau 2")
elif IMC >= 40:
    print("Obesidade Grau 3")

