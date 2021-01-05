"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as características do objeto.
    - Métodos (funções) -> Representam os comportamentos/ações do objeto.

Em Python, para definir uma classe, utilizamos a palavra reservada "class".

OBS 1: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado.
OBS 2: Quando nomeamos nossas classes, por convenção, a primeira letra da palavra é maiúscula. Em nomes compostos,
       utilizar CamelCase, todas as palavras juntas.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


lamp = Lampada()
print(type(lamp))  # <class '__main__.Lampada'>
