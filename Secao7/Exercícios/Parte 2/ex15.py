from random import choice
gabarito = ['a', 'c', 'd', 'd', 'b', 'c', 'b', 'a', 'd', 'c']

respostas = []
pontos = {}

for i in range(5):
    row = list(choice(['a', 'b', 'c', 'd']) for _ in range(10))
    respostas.append(row)

for index_row, i in enumerate(respostas):
    aux = 0
    for index_col, j in enumerate(i):
        if j == gabarito[index_col]:
            aux = aux + 1
        print(j, end=" ")
    pontos.update({index_row: aux})
    print()

print(pontos)
