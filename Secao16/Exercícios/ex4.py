class Televisao:

    def __init__(self, marca):
        self.__marca = marca
        self.__volume = 0
        self.__canal = 1

    def get_marca(self):
        return self.__marca

    def get_volume(self):
        return self.__volume

    def set_volume(self, op):
        if op == "+":
            if self.__volume < 100:
                self.__volume = self.__volume + 1
            else:
                print("O volume só pode ser de 0 a 100!")
        else:
            if self.__volume > 0:
                self.__volume = self.__volume - 1
            else:
                print("O volume só pode ser de 0 a 100!")

    def get_canal(self):
        return self.__canal

    def set_canal(self, **kwargs):
        if 'canal' in kwargs:
            if kwargs['canal'] >= 1:
                self.__canal = kwargs['canal']
        elif 'up' in kwargs:
            self.__canal = self.__canal + 1
        else:
            if self.__canal > 1:
                self.__canal = self.__canal - 1


class ControleRemoto:

    def __init__(self, televisao):
        self.__televisao = televisao

    def aumentar_volume(self):
        self.__televisao.set_volume("+")

    def diminuir_volume(self):
        self.__televisao.set_volume("-")

    def mudar_canal(self, **kwargs):
        self.__televisao.set_canal(**kwargs)

    def get_volume(self):
        return self.__televisao.get_volume()

    def get_canal(self):
        return self.__televisao.get_canal()


TV = Televisao("Samsung")
ctrl = ControleRemoto(TV)
print(f"Canal: {ctrl.get_canal()}")
ctrl.mudar_canal(canal=10)
print(f"Canal: {ctrl.get_canal()}")
ctrl.mudar_canal(up=True)
print(f"Canal: {ctrl.get_canal()}")

print(f"Volume: {ctrl.get_volume()}")
ctrl.aumentar_volume()
print(f"Volume: {ctrl.get_volume()}")
ctrl.aumentar_volume()
print(f"Volume: {ctrl.get_volume()}")
ctrl.aumentar_volume()
print(f"Volume: {ctrl.get_volume()}")
ctrl.aumentar_volume()
print(f"Volume: {ctrl.get_volume()}")
ctrl.diminuir_volume()
print(f"Volume: {ctrl.get_volume()}")
