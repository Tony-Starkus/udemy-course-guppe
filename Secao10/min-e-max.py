"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos
min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

# Exemplos
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # print: 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))  # print: 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))  # print: 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))  # print: f | Ele escolhe a chave

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))  # print: 129

print(max(3, 34))  # Entre dois valores, qual o maior? | print: 34

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))

# Podemos passar N valores
print(max(4, 67, 54))
print(max('a', 'ab', 'abc'))  # print: abc
print(max('a', 'b', 'c', 'g'))  # print: g
print(max(3.125, 5.789))
print(max('Geek University'))  # print: y


------------------------------------------------------------------------------------------------------------------------
min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos
# Exemplos
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))  # print: 1

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))  # print: 1

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))  # print: 1

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))  # print: a | Ele escolhe a chave

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))  # print: 1

print(min(3, 34))  # Entre dois valores, qual o menor? | print: 3

# Faça um programa que receba dois valores do usuário e mostre o menor
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))

# Podemos passar N valores
print(min(4, 67, 54))
print(min('a', 'ab', 'abc'))  # print: a
print(min('a', 'b', 'c', 'g'))  # print: a
print(min(3.125, 5.789))
print(min('Geek University'))  # print: ' ' <- espaço

# Outros exemplos
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))  # Tim -> Porque ele organiza em ordem alfábetica.
print(min(nomes))  # Arya
print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim


print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))


musicas = [
    {"Titulo": "Thuderstruck", "tocou": 3},
    {"Titulo": "Dead Skin Mask", "tocou": 2},
    {"Titulo": "Back in Black", "tocou": 4},
    {"Titulo": "Too old to rock'in'roll", "tocou": 32}
]

# DESAFIO! Imprima somente o título da música mais tocada e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['Titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['Titulo'])

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?!
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['Titulo'])

min = 99999999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['Titulo'])
"""

musicas = [
    {"Titulo": "Thuderstruck", "tocou": 3},
    {"Titulo": "Dead Skin Mask", "tocou": 2},
    {"Titulo": "Back in Black", "tocou": 4},
    {"Titulo": "Too old to rock'in'roll", "tocou": 32}
]

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?!
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['Titulo'])

min = 99999999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['Titulo'])
