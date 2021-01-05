"""
Doctests

Para rodar um teste do doctest: $ python -m doctest -v nome_do_modulo.py



"""


def soma(a, b):
    """
    Soma os números a e b
    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    """
    return a + b


print(soma(3, 4))


# Outro exemplo, aplicando o TDD
def duplicar(valores):
    """
    Dupliccar os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 5, 8]

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return []
