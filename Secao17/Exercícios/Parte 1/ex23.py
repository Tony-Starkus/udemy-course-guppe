
class Televisor:

    def __init__(self, ligado=False, volume=0, canal=1, numero_canais=10, volume_maximo=100):
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume
        self.__numero_canais = numero_canais
        self.__volume_maximo = volume_maximo

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
        print("A TV está ligada.")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
        print('A TV está desligada.')

    def imprimir(self):
        print(f"Ligado: {self.__ligado} | Canal: {self.__canal} | Max. Canal: {self.__numero_canais} "
              f"| Volume: {self.__volume} | Max. Volume: {self.__volume_maximo}")


tv1 = Televisor()
tv1.imprimir()
