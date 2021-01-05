
class Quadrado:

    def __init__(self, lado):
        self.lado = lado
        self.area = "Não calculado"
        self.perimetro = "Não calculado"

    def imprimir(self):
        print(f"Lado: {self.lado} | Área: {self.area} | Perímetro: {self.perimetro}")

    def calcular_area(self):
        self.area = self.lado * self.lado

    def calcular_perimetro(self):
        self.perimetro = 4 * self.lado


q1 = Quadrado(5)
q1.imprimir()
q1.calcular_area()
q1.imprimir()
q1.calcular_perimetro()
q1.imprimir()

