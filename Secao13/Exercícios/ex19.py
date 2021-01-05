import names
from random import randint


def create_file():
    with open("ex19_dados.txt", "w") as file1:
        for i in range(15):
            file1.write(f"NOME: {names.get_first_name()} NOTA: {randint(0, 10)}\n")


# Criar arquivos com os dados.
# create_file()

with open("ex19_dados.txt") as file:
    dados = dict()
    for line in file.readlines():
        line = line.split(" ")
        dados.update({line[1]: int(line[3])})
    print(f"{max(dados, key=dados.get)} tem a maior nota: {dados[max(dados, key=dados.get)]}")
