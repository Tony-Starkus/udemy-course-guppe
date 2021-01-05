"""
Escrevendo em arquivos CSV
writer

writerow() -> Escreve uma linha. Recebe uma lista como parâmetro
from csv import writer

with open("filmes.csv", "a") as file:
    escritor_csv = writer(file)
    filme = None
    escritor_csv.writerow(["Título", "Gênero", "Duração"])
    while file != "sair":
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow([filme, genero, duracao])
        else:
            break
"""

# DictWriter

from csv import DictWriter

with open("filmes.csv", "w") as file:
    cabecalho = ["Título", "Gênero", "Duração"]
    escritor_csv = DictWriter(file, fieldnames=cabecalho)
    escritor_csv.writeheader()

    filme = None
    while filme != "sair":
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            # OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
        else:
            break
