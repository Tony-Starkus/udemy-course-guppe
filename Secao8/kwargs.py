"""
**kwargs

Poderíamos chamar este padrão de **xis, mas por convenção chamados de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizamos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.


# Exemplo 1


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de pessoa {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e *kwargs não são obrigatórios




# Exemplo 2 - Mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))



# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios:
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs





def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao('20', 'Thalisson', solteiro=True)
minha_funcao('19', 'Thalisson', 4, 5, 3, solteiro=True)
minha_funcao('19', 'Carla', eu='Não', java='False', python='True')  # Esses atributos entram no **kwargs.






# Entenda por que é importante manter a ordem dos parâmetros na declaração


# def mostra_info(a, b, *args, instrutor='Geek', **kwargs):  # Função com a ordem correta de parâmetros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):  # Função com a ordem de parâmetros incorreta
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

a = 1
b = 2
*args = 3
instrutor = 'Geek'
**kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
"""

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Thalisson', 'sobrenome': 'Bandeira'}
print(mostra_nomes(nome='Brad', sobrenome='Pitty'))
print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# OBS! Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função
