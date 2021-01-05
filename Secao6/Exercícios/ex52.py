saque = int(input("Informe o valor do saque: "))
notas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

while saque >= 100:
    notas[100] = notas[100] + 1
    saque = saque - 100
while saque >= 50:
    notas[50] = notas[50] + 1
    saque = saque - 50
while saque >= 20:
    notas[20] = notas[20] + 1
    saque = saque - 20
while saque >= 10:
    notas[10] = notas[10] + 1
    saque = saque - 10
while saque >= 5:
    notas[5] = notas[5] + 1
    saque = saque - 5
while saque >= 2:
    notas[2] = notas[2] + 1
    saque = saque - 2
while saque >= 1:
    notas[1] = notas[1] + 1
    saque = saque - 1

for nota, value in notas.items():
    if value > 0:
        print(f"{value} notas de {nota}")
