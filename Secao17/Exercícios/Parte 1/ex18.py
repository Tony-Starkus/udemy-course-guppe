
class Eletrodomestico:

    def __init__(self, ligado):
        self.__ligado = ligado

    def imprimir(self):
        print(f"Ligado: {self.ligado}")


e1 = Eletrodomestico()
e1.imprimir()
