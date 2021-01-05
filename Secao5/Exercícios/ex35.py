data = input("Digite a data no formado dia/mes/ano: ").split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
bisexto = None

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    bisexto = True
else:
    bisexto = False
print(bisexto)
if mes not in range(1, 13):
    print("Mês inválido")
    exit()

if mes == 2:
    if bisexto:
        print("AQUI")
        if dia not in range(1, 30):
            print("Dia inválido")
            exit()
    else:
        print("AQUI 2")
        if dia not in range(1, 29):
            print("Dia inválido")
            exit()
else:
    if dia not in range(1, 32):
        print("Dia inválido")
        exit()

print("Data válida")
