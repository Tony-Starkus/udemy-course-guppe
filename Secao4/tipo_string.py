"""
Tipo string

Em python, um dado é considerado do tipo string sempre que:
- Estiver entre áspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre áspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre  áspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

Histórico{

nome = "Gina's bar"
print(nome)
print(type(nome))

nome = 'Angelina\nJolie'
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())

nome = 'Geek University'
print(nome.split())  # Transforma em uma lista de string. Ex: ['Geek', 'University']

}

OBS: em uma string de áspas duplas ex: "Oi", se quiser imprimir uma aspas duplas, usa o \. ex: "O\"i".
nome = "Angelina \" Jolie"
print(nome)
print(type(nome))
"""
# - Estiver entre áspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14]

nome = 'Geek University'

print(nome[0:4])  # Nome da operação: Slice de string

print(nome[5:15])  # Vai imprimir a string começando na posição indicada e terminando na posição indicada

print(nome.split()[0])  # Acessando a posição 0 da lista: ['Geek', 'University'] | [0, 1]

# [::-1] -> Começe do primeiro elemento, vá até o último elemento e inverta
print(nome[::-1])  # Inversão da string. Saida: ytisrevinU keeG

print(nome[2].isdigit())

print(nome.replace('e', 'i'))

nome = 'ana'
print(nome)
print(nome[::-1])
