idade = int(input("Informe a idade: "))

if idade < 5:
    print("Sem classificação")
elif idade in range(5, 8):
    print("Infantil A")
elif idade in range(8, 11):
    print("Infantil B")
elif idade in range(11, 14):
    print("Juvenil A")
elif idade in range(14, 18):
    print("Juvenil B")
elif idade >= 18:
    print("Sênior")
