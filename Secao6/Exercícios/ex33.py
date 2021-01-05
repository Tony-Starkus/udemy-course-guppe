from sys import maxsize

n = int(input("Informe o valor de N: "))
i = int(input("Informe o valor de I: "))

if i < 1:
    print("O valor não pode ser menor que 1")
    exit()

j = int(input("Informe o valor de J: "))
if j < 1:
    print("O valor não pode ser menor que 1")
    exit()

valores = list()

for x in range(maxsize):
    if x % i == 0 or x % j == 0:
        valores.append(x)
    if len(valores) == n:
        break;
print(valores)
