"""
Funções com retorno
------------------------------------------------------------------------------------------------------------------------
OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é 'None'.
def quadrado_de_7():
    print(7 * 7)
ret = quadrado_de_7()
print(ret)
------------------------------------------------------------------------------------------------------------------------
OBS: Funções Python que retornam valores, devem retornar estes valores com palavra reservada 'return'.
OBS: Não precisamos nescessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução
da função para outras funções.
def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno {quadrado_de_7() + 1}')
------------------------------------------------------------------------------------------------------------------------
def diz_oi():
    return 'Oi '


alguem = 'Pedro'
print('{} {}'.format(diz_oi(), alguem))
print(diz_oi() + alguem)
------------------------------------------------------------------------------------------------------------------------
OBS: Sobre a palavra reservada return:
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores.

# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;


def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi! '
    print('Estou sendo executado após o retorno...')


print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferentes returns;


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores.


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
print(outra_funcao())




# Vamos criar uma função para jogar a moeda
from random import random


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

"""

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False


print(eh_impar())
