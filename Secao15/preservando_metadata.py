"""
Preservando metadatas com wraps

Metadados -> São dados intrísecos em arquivos
    - Nome
    - Tipo/Extensão
    - Tamanho

Wraps -> São funções que envolvem elementos com diversas finalidades.



# Problema
def ver_log(funcao):
    def logar(*args, **kwargs):
        Eu sou uma função (loga) dentro de outra
        print(f"Você está chamando {funcao.__name__}")
        print(f"Aqui a documentação: {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    Soma dois números.
    return a + b


# print(soma(10, 30))
print(soma.__name__)
print(soma.__doc__)

"""
from functools import wraps


# Resolvendo o Problema
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (loga) dentro de outra"""
        print(f"Você está chamando {funcao.__name__}")
        print(f"Aqui a documentação: {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


# print(soma(10, 30))
print(soma.__name__)
print(soma.__doc__)
