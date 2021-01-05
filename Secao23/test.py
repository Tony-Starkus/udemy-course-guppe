import random

NAIPES = '♠ ♥ ♣ ♦ ♤ ♡ ♧ ♢'.split()  # Constante
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()  # Constante


def criar_baralho(aleatorio=False):
    """
    Cria um baralho com 52 cartas
    :param aleatorio:
    :return: list
    """
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    print(baralho)
    print(baralho[0::4])
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


baralho = criar_baralho()
distribuir_cartas(baralho)
