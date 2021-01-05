"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)
________________________
|Python|Módulos Builtin|
------------------------


# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())


# Podemos importar todas as funções de um módulo utilizando o *
from random import *
print(random())


# Utilizando alias (apelidos) para módulos/funções
from random import randint as rdi
print(rdi(5, 89))

https://docs.python.org/3/py-modindex.html
"""

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(3, 7))
lista = [1, 2, 3]
shuffle(lista)
print(lista)
print(choice('Geek'))
