
class Elevador:

    andar = 0
    andares = int(input("Informe o número de andares (excluindo o térreo): "))
    capacidade = int(input("Informe a capadidade de pessoas no elevador: "))
    pessoas = 0

    @classmethod
    def mover(cls):
        if cls.pessoas < cls.capacidade:
            aux = int(input("Informe para qual andar deseja ir: "))
            if cls.andares >= aux >= 0:
                cls.andar = aux
                print(f"Andar atual é: {cls.andar}")
            else:
                print(f"O elevador não ir para o andar {aux}. O prédio só tem {cls.andar} andares")
        else:
            print("O número de pessoas no elevador ultrapassa sua capacidade!")

    @classmethod
    def pessoas(cls):
        cls.pessoas = int(input("Informe quantas pessoas tem no elevador: "))


Elevador.mover()
