"""
Por que testar nosso código?

Testes Automatizados!
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f"{self.__nome} está miando...")
