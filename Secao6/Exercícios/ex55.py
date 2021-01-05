from sys import maxsize
num = int(input("Informe um número inteiro: "))

if num < 0:
    print("O número não pode ser negativo!")
    exit()

valores = []
for i in range(2, maxsize):
    primo = True
    for j in range(i, 0, -1):
        if j != 1 and j != i:
            if i % j == 0:
                primo = False
                break
    if primo:
        valores.append(i)
    if len(valores) == num:
        break

print(sum(valores))
