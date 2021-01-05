altura_degrau = float(input("Altura do degrau: "))
altura_desejada = float(input("Altura a ser alcançada: "))
x = False
resposta = 0
altura_atual = 0
while not x:
    if altura_atual < altura_desejada:
        altura_atual = altura_atual + altura_degrau
        resposta = resposta + 1
    else:
        x = True
print(f"Total de desgraus para escalar: {resposta}")
