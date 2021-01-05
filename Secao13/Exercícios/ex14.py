"""
- Uma biblioteca para gerar nomes aleatórios
    $ pip install names
"""
import names
from random import randint
from datetime import date


def idade(data):
    hoje = date.today()
    age = hoje.year - int(data[2]) - ((hoje.month, hoje.day) < (int(data[1]), int(data[0])))
    return age


def criar_arquivo():
    with open("ex14_dados.txt", "w") as file:
        for i in range(10):
            file.write(f"{names.get_full_name()} {randint(1, 30)} {randint(1, 12)} {randint(1930, 2019)}\n")


# Função para criar os dados
# criar_arquivo()


with open("ex14_dados.txt") as file1:
    with open("ex14_dados_processados.txt", "w") as file2:
        for line in file1.readlines():
            file2.write(f"{line.split(' ')[0]} {line.split(' ')[1]} "
                        f"{idade([line.split(' ')[i] for i in range(2, 5)])} anos\n")
