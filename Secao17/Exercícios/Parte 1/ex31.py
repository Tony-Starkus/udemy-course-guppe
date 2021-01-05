
class Microondas:

    def __init__(self):
        self.__ligado = False
        self.__porta_fechada = True

    def ligar(self):
        if not self.__porta_fechada:
            print("O microondas está com a porta aberta!")
            return
        if not self.__ligado:
            self.__ligado = True
        print("O microondas está ligado!")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
        print("O microodas está desligado!")

    def abrir_porta(self):
        self.__porta_fechada = False

    def fechar_porta(self):
        self.__porta_fechada = True

    def imprimir(self):
        print(f"Ligado: {self.__ligado} | Porta Fechada: {self.__porta_fechada}")


m1 = Microondas()
m1.abrir_porta()
m1.ligar()
m1.imprimir()
