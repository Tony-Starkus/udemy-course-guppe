"""
Lendo arquivos CSV

CSV: Comma Separated Values - Valores Separados por Vírgula

# Site para conseguir dados
http://dados.gov.br/dataset


with open("lutadores.csv") as file:
    dados = file.read()
    # print(type(dados))
    dados = dados.split(",")
    print(dados)



A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivos csv como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivos CSV como OrderedDicts;



from csv import reader

with open('lutadores.csv') as file:
    leitor_csv = reader(file)
    next(leitor_csv)  # Pulando cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f"{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros")
"""
from csv import DictReader

with open('lutadores.csv') as file:
    leitor_csv = DictReader(file)
    next(leitor_csv)  # Pulando cabeçalho
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} centímetros")
