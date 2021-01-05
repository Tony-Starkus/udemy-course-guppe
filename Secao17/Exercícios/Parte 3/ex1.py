"""
Pacote: Sobrecarga
"""


class Pessoa:

    def __init__(self, codigo, nome, idade):
        print("Construtor Padrão")
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    def exibe(self, show_age=1):
        if show_age:
            print(f"Código: {self.__codigo} | Nome: {self.__nome} | Idade: {self.__idade}")
        else:
            print(f"Código: {self.__codigo} | Nome: {self.__nome}")


class TestaPessoa(Pessoa):

    def __init__(self, codigo, nome, idade):
        super().__init__(codigo, nome, idade)

    def exibe(self, show_age=1):
        super().exibe(show_age)


tp = TestaPessoa(1, "Thalisson", 21)
tp.exibe()
