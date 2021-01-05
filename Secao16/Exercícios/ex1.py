
class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura


p1 = Pessoa("Thalisson", 1.65, 21)
print(p1.__dict__)
p1.set_nome("Thalisson Bandeira Araújo")
print(p1.get_nome())
print(p1.get_idade())
print(p1.get_altura())
