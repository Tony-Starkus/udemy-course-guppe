from random import choice
gabarito = ['a', 'e', 'd', 'e', 'b', 'c', 'b', 'a', 'd', 'c']

respostas = {}

for i in range(3):
    matricula = int(input("Informe a matrícula: "))
    aux = [choice(gabarito) for _ in range(10)]
    nota = 0
    for index, item in enumerate(aux):
        if item == gabarito[index]:
            nota = nota + 1
    respostas.update({matricula: [aux, nota]})

for i in respostas.items():
    print(i)
