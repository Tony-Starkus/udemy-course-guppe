intervalo = list(map(int, input("Defina o intervalo, separado por espaço: ").split(" ")))
x = 0
if intervalo[0] > intervalo[1]:
    print("Intervalo de valores inválido")
else:
    for i in range(intervalo[0], intervalo[1] + 1):
        if i % 2 == 1:
            x = x + i
    print(x)
