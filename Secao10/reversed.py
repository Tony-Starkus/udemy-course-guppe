"""
Reversed

OBS: Não confunda com a função reverse(), que estudamos nas listas
!!!!A função reverse() só funciona em listas!!!!
!!!!!Já a função reversed() funciona com qualquer iterável!!!!!
"""

# Exemplos
lista = [1, 2, 3, 4, 5]

res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list((reversed(lista))))

# Tupla
print(tuple(reversed(lista)))

# Conjunto
# OBS: EM conjuntos, não definimos a ordem dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end=' ')
print('\n')
# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Podemos também utilizar o reversed() para fazer um loop for revero
for n in reversed(range(0, 10)):
    print(n)

# Apesar que também já vimos como fazer isso utilizando o própio range()
for n in range(9, -1, -1):
    print(n)
