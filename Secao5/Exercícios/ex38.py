data = input("Digite a data separado por espaços: ").split(" ")

if len(data[0]) > 3:
    print("Data inválida")
    exit()
if len(data[1]) > 3:
    print("Data inválida")
    exit()
if len(data[2]) != 4:
    print("Data inválida. Digite o ano com 4 dígitos!")
    exit()

dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
bisexto = None

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    bisexto = True
else:
    bisexto = False

if dia not in range(1, 32):
    print("Data inválida")
    exit()
else:
    if mes not in range(1, 13):
        print("Data inválida")
        exit()
    else:
        if mes == 2:
            if bisexto:
                if dia > 29:
                    print("Data inválida")
                    exit()
            else:
                if dia > 28:
                    print("Data inválida")
                    exit()

print("Data válida")
