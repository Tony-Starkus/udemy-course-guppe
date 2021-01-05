from math import sqrt


def quadrado_perfeito(x):
    if sqrt(x).is_integer():
        print("É quadrado perfeito")
    else:
        print("Não é quadrado perfeito")


quadrado_perfeito(1)
quadrado_perfeito(2)
quadrado_perfeito(4)
