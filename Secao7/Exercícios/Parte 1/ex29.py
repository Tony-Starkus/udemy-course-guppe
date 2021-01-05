valores = []

for i in range(6):
    valores.append(int(input("Digite um número inteiro: ")))

# print([x for x in valores if x % 2 == 0])
# Números pares digitados
print(list(filter(lambda x: x % 2 == 0, valores)))
# Soma dos pares digitados
print(sum([x for x in valores if x % 2 == 0]))
# Números ímpares digitados
print(list(filter(lambda x: x % 2 == 1, valores)))
# Quantidade de ímpares digitados
print(len(list(filter(lambda x: x % 2 == 1, valores))))
