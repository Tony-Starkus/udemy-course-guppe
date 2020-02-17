"""
Listas (list)

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; OU seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

Listas são mutáveis. Elas podem mudar constantemente.
"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente inverter uma lista
lista1.reverse()
lista2.reverse()
"""
Outra forma: print(lista1[::-1]) <- slice
"""
print(lista1)
print(lista2)

# Podemos facilmente checar e determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista em ordem crescente/alfabética
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista5.count('e'))

# Adicionar elementos em listas
"""
Para adicionar elementos em listas, utilizamos a função append
"""
print(lista1)
lista1.append(42)
print(lista1)
# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
lista1.append([8, 3, 1])
print(lista1)

if[8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')


lista1.extend([123, 44, 67])  # Adicionar os valores de uma lista dentro de outra lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice -> .insert(posicao, valor_a_inserir)
# O valor na posição atual não é substituido, é deslocado para a direita.
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas | Igual ao .extend(), mas no extend não é nescessário criar uma nova lista.
lista6 = lista1 + lista2
print(lista6)

# Copiar uma lista
lista7 = lista2.copy()
print(lista7)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista6))

# Podemos remover facilmente o ultimo elemento de uma lista
# Os elementos são deslocados para a esquerda. A posição removida não fica vazia
print(lista5)
lista5.pop()  # O .pop() além de remover o ultimo elemento, ele também retorna o valor do elemento removido.
print(lista5)

# Podemos remover um elemento pelo índice
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos. Ou seja, deixar ela vazia
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista
# Exemplo 1 | O .split() separa os elementos pelo espaço, por padrão
curso = 'Programação em Python: Essencial'
print(curso.split())
# Exemplo 2
curso = "Programação,em,Python:,Essencial"
print(curso.split(','))

# Convertendo uma lista em uma string
lista8 = ['Programação', 'em', 'Python:', 'Essencial']
curso = ' '.join(lista8)  # Pega a lista6 e coloca espaço entre cada elemento, transformando em string
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista9 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]
print(lista9)

"""
# Iterando sobre listas
# Exemplo 1 - Utilizando for
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)


for produto in carrinho:
    print(produto)
"""

# Utilizando variáveis em listas
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Em listas, fazemos acesso aos elementos de forma indexada
#           0         1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# Pense na lista como uma roda/círculo, onde o último elemento da lista está ligado ao início da lista
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5])  Erro, pois não existe índice -5

"""
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
"""

# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Outros métodos não tão importantes, mas também úteis

# 1. Encontrar um índice de um elemento na lista
numeros = [5, 5, 6, 7, 8, 9, 10]
print(numeros.index(6))  # Em qual índice da lista está o valor 6
print(numeros.index(9))  # Em qual índice da lista está o valor 9
print(numeros.index(5))  # Retorna o índice do primeiro elemento encontrado
# Caso não tenha o elemento na lista, será apresentado erro

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1))  # Procurar o numero 5 a partir do índice 1

# Podemos fazzer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o índice do valor 8, entre os índices 3 a 6


# Revisão de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'inicio'
lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no índice 1 e indo até o final.

# Trabalhando com slice de lista com o parâmetro 'fim'
print(lista[:2])  # Iniciando no índice 0 e indo até o índice (2 - 1).

# Trabalhando com slice de lista com o parâmetro 'passo'.
print(lista[1::2])  # Começa no índice 1, vai até o final, de 2 em 2.


# Invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes.reverse()
print(nomes)


# *Soma; *Valor Máximo, *Valor Mínimo, Tamanho
# * Se os valores forem todos inteiros ou reais.
lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))


# Transformar uma lista em tupla
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
# Se tivermos mais elementos para desempacotar do que variáveis, vai dar erro. O contrário também.


# Copiando uma lista para outra (Shallow Copy e Deep Copy)
lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)
# Veja que ao utilizarmos lista.copy(), criamos uma nova lista que não se afetam (Deep Copy).


nova = lista
nova.append(4)
print(nova)
print(lista)
# Veja que utilizamos a cópia via atribuição. Uma modificação feita em uma altera a outra (Shallow Copy).
