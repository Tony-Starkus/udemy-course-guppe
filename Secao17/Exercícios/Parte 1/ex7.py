from math import pi


class Circulo:

    def __init__(self, raio):
        self.raio = raio
        self.area = "Não calculado"
        self.perimetro = "Não calculado"

    def calcular_area(self):
        self.area = pi * self.raio * self.raio

    def calcular_perimetro(self):
        self.perimetro = 2 * pi * self.raio

    def imprimir(self):
        print(f"Raio: {self.raio} | Área: {self.area} | Perímetro: {self.perimetro}")


c1 = Circulo(5)
c1.imprimir()
c1.calcular_area()
c1.imprimir()
c1.calcular_perimetro()
c1.imprimir()

