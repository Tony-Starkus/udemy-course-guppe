
class Televisor:

    def __init__(self, ligado=False, volume=0, canal=1):
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume

    def imprimir(self):
        print(f"Ligado: {self.__ligado} | Canal: {self.__canal} | Volume: {self.__volume}")


tv1 = Televisor()
tv1.imprimir()
