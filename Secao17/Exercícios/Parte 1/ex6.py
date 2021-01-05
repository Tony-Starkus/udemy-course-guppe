
class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        self.area = "Não calculado"
        self.perimetro = "Não calculado"

    def calcular_area(self):
        self.area = self.comprimento * self.largura

    def calcular_perimetro(self):
        self.perimetro = (2 * self.comprimento) + (2 * self.largura)

    def imprimir(self):
        print(f"Comprimento: {self.comprimento} | Largura: {self.largura} | Área: {self.area} | "
              f"Perímetro: {self.perimetro}")


r1 = Retangulo(20, 8)
r1.imprimir()
r1.calcular_area()
r1.imprimir()
r1.calcular_perimetro()
r1.imprimir()
