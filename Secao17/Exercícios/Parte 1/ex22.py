
class Televisor:

    def __init__(self, ligado=False, volume=0, canal=1):
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
        print("A TV está ligada.")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
        print('A TV está desligada.')

    def imprimir(self):
        print(f"Ligado: {self.__ligado} | Canal: {self.__canal} | Volume: {self.__volume}")


tv1 = Televisor()
tv1.imprimir()
