
class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

    def imprimir(self):
        print(f"Marca: {self.__marca} | Modelo: {self.__modelo} | Cor: {self.__cor} | Marcha: {self.__marcha}")


m1 = Moto("Honda", "HX10", "Vermelho", 1)
m1.imprimir()
