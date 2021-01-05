vetor = []

for i in range(5):
    vetor.append(float(input("Informe um número: ")))

op = input("0 - Finalizar\n"
           "1 - Imprimir na ordem direta\n"
           "2- Imprimir na ordem inversa")

if op == 0:
    exit()
elif op == 1:
    print(vetor)
elif op == 2:
    print(list(reversed(vetor)))
else:
    print("Código Inválido")
