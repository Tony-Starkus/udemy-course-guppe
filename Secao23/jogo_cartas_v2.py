import random
from typing import Dict, List, Tuple, Set

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
    # baralho[inicio::passo]
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {n: m for n, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f"{jogador}: {carta}")


baralho = criar_baralho(True)
print(distribuir_cartas(baralho))

jogar()

if __name__ == '__main__':
    jogar()
