"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa
pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema



# Exemplo 1 - Tratando um erro genérico
try:
    geek()
except:
    print("Deu algum problema")


# Exemplo 2 - Tratando um erro genérico
try:
    len(5)
except:
    print("Deu algum problema")


# Exemplo 3 - Tratando um erro específico
try:
    geek()
except NameError:
    print("Você está utilizando uma função inexistente")


# Exemplo 4 - Tratando um erro específico
try:
    len(5)
except TypeError:
    print("Você está utilizando uma função inexistente")


# Exemplo 5 - Tratando um erro específico
try:
    len(5)
except TypeError as err:
    print(f"A aplicaçao gerou o seguinte erro: {err}")


# Exemplo 6 - Tratando um erro específico
try:
    geek()
except NameError as erra:
    print(f"Deu NameError: {erra}")
except TypeError as errb:
    print(f"Deu TypeError: {errb}")
except:
    print("Deu um erro diferente")


OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma
específica.
"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Geek"}
print(pega_valor(dic, "nome"))
print(pega_valor(dic, "game"))
print(pega_valor(7, "nome"))
print(pega_valor(dic, 9))
