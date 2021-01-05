
class Eletrodomestico:

    def __init__(self, ligado):
        self.__ligado = ligado

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
        print("O aparelho está ligado.")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
        print("O aparelho está desligado")

    def imprimir(self):
        print(f"Ligado: {self.__ligado}")


e1 = Eletrodomestico(False)
e1.imprimir()
e1.ligar()
e1.imprimir()

