"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde comece
com arterísco.

Exemplo:
*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O parâmetro *args utilizando em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde
já lembre-se que tuplas são imutáveis.


# Entendendo o *args
def soma_todos_numero(nome, email, *args):
    # total = 0
    # for numero in args:
    #     total = total + numero
    # return total
    return sum(args)


print(soma_todos_numero('Angelina', 'Jolie'))
print(soma_todos_numero('Angelina', 'Jolie', 1))
print(soma_todos_numero('Angelina', 'Jolie', 2, 3))
print(soma_todos_numero('Angelina', 'Jolie', 2, 3, 4))
print(soma_todos_numero('Angelina', 'Jolie', 3, 4, 5, 6))



def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    else:
        return 'Eu não tenho certeza quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

"""


def soma_todos_numero(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]
# print(soma_todos_numero(numeros))  # print(args) => ([1, 2, 3, 4, 5, 6, 7],)

# Desempacotador
# num1, num2, num3, num4, num5, num6, num7 = numeros
# print(soma_todos_numero(num1, num2, num3, num4, num5, num6, num7))
print(soma_todos_numero(*numeros))

# OBS: O asterísco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados. Desta
# forma ele saberá que precisará antes desempacotar estes dados.
