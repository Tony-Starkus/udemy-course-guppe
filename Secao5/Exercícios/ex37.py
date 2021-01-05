chegada = input("Digite a hora da chegada: ").split(" ")
hora_chegada = int(chegada[0])
minuto_chegada = int(chegada[1])

if hora_chegada not in range(0, 25):
    print("A hora não é válida")
elif minuto_chegada not in range(0, 60):
    print("O minuto não é válido")

partida = input("Digite a hora da partida: ").split(" ")
hora_partida = int(partida[0])
minuto_partida = int(partida[1])

if hora_partida not in range(0, 25):
    print("A hora não é válida")
elif minuto_partida not in range(0, 60):
    print("O minuto não é válido")

cada = 0
if hora_partida > hora_chegada:
    tempo = hora_partida - hora_chegada
    if minuto_partida != 0:
        tempo = tempo + 1

    if tempo <= 2:
        cada = 1
    elif tempo in range(3, 5):
        cada = 1.40
    else:
        cada = 2
    print(f"Preço: {tempo * cada}")

else:
    tempo = 24 + (hora_partida - hora_chegada)
    if minuto_partida != 0:
        tempo = tempo + 1

    if tempo <= 2:
        cada = 1
    elif tempo in range(3, 5):
        cada = 1.40
    else:
        cada = 2

    print(f"Preço: {tempo * cada}")
