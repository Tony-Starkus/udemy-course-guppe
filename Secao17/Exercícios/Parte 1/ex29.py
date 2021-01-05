
class Microondas:

    def __init__(self, ligado=False):
        self.__ligado = ligado
        self.__porta_fechada = True

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
        print("O microondas está ligado!")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
        print("O microodas está desligado!")

    def porta_fechada(self, value):
        self.__porta_fechada = value

    def imprimir(self):
        print(f"Ligado: {self.__ligado} | Porta Fechada: {self.__porta_fechada}")


m1 = Microondas()
m1.ligar()
m1.imprimir()
