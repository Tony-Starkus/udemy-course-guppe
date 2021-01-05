"""
Pacote: Herança
"""


class Equipamento:

    def __init__(self, teclado, mouse):
        self.__teclado = teclado
        self.__mouse = mouse

    def set_teclado(self, teclado):
        self.__teclado = teclado

    def set_mouse(self, mouse):
        self.__mouse = mouse

    def exibe(self):
        print(f"Teclado: {self.__teclado} | Mouse: {self.__mouse}")


class Computador(Equipamento):

    def __init__(self, ram, hd, teclado, mouse):
        super().__init__(teclado, mouse)
        self.__ram = ram
        self.__hd = hd

    def exibe(self):
        print(f"Computador: ram = {self.__ram} | hd = {self.__hd}")
        super().exibe()


class TestaEquipamento:
    if __name__ == '__main__':
        eqp1 = Equipamento(True, True)
        pc = Computador(8, 1000, True, True)
        eqp1.exibe()
        pc.exibe()
