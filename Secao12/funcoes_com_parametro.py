"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

========================================================================================================================
# Refatorando uma função


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))
========================================================================================================================
def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva a/o {aniversariante}!')


cantar_parabens('Patrícia')
========================================================================================================================
# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função quantos parâmetros
# forem necessários. Eles são separados por vírgula.

# Exemplo


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))
print(multiplica(4, 5))
print(multiplica(2, 8))
print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

"""


def soma(a, b):
    return a + b

# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


if __name__ == '__main__':
    print(nome_completo(nome='Angelina', sobrenome='Jolie'))
else:
    print("O módulo funcoe_com_parametro foi importado.")
