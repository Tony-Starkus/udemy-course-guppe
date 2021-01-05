"""
Módulo random e o que são modulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.


# Existe duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (Não recomendado).
import random
# Ao realizar o import de todo o módulo. Todas as funções, atributos, e classes e propriedades que estiverem dentro
# do módulo, ficarão disponíveis (Ficaram em memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

# random() -> Gera um número pseudo-aleatório entre 0 e 1.
# # # print(random.random())
# Veja que para utilizar a função random(), nós colocamos o nome do pacote e o nome da função, separados por ponto (.)
# OBS: Não confuda a função random() com o pacote random.



# Forma 2 - Importando uma função específica do módulo (Recomendada).
from random import random
# No import acima, estamos falando: Do módulo random, importe a função random()
for i in range(10):
    print(random())



# uniform() -> Gerar um número Real pseudo-aleatório entre os valores estabelecidos
from random import uniform
for i in range(10):
    print(uniform(3, 7))  # O número 7 não é incluido. Vai ser sempre entre 3 e 6.9999999[...]



# randint() -> Gera valores Inteiros pseudo-aleatórios entre os valores estabelecidos.
from random import randint
# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em um e vai até 60




# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
print(choice('Geek University'))
"""

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)  # Embaralhando as cartas
print(cartas)
# print(cartas.pop())
