
class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

    def marcha_acima(self):
        if self.__marcha < 5:
            self.__marcha += 1
        else:
            print("A moto está na marcha mais alta!")

    def marcha_abaixo(self):
        if self.__marcha > 1:
            self.__marcha -= 1
        else:
            print("A moto está na marcha mais baixa!")

    def imprimir(self):
        print(f"Marca: {self.__marca} | Modelo: {self.__modelo} | Cor: {self.__cor} | Marcha: {self.__marcha}")


m1 = Moto("Honda", "HX10", "Vermelho", 1)
m1.marcha_acima()
m1.imprimir()
m1.marcha_acima()
m1.imprimir()
m1.marcha_abaixo()
m1.imprimir()
