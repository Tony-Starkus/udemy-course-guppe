# O algoritmo falha em número negativos!
intervalo = list(map(int, input("Informe o intervalo, separado por espaço: ").split(" ")))

valores = []
for i in range(intervalo[0], intervalo[1] + 1):
    if i in (0, 1):
        continue
    primo = True
    for j in range(i - 1, 1, -1):
        if i % j == 0:
            primo = False
            break

    if primo:
        valores.append(i)

print(sum(valores))
