
class Microondas:

    def __init__(self, ligado=False):
        self.__ligado = ligado

    def imprimir(self):
        print(f"Ligado: {self.__ligado}")


m1 = Microondas()
m1.imprimir()
