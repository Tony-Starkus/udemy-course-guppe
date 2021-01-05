"""
POO - O método super()

O método super() se refere à super classe

"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} animal fala {som}")


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)  # NÃO IDEAL. MAS PODE SER FEITO!
        super().__init__(nome, especie)  # IDEAL!
        self.__raca = raca


felix = Gato("Felix", "Felino", "Angorá")
felix.faz_som("miau")
