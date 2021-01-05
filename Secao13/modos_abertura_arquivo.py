"""
Modos de Abertura de Arquivo

r -> Abre para leitura. <- padrão.
w -> Abre para escrita. <- Sobrescreve caso o arquivo já exista.
x -> Abre para escrita somente se o arquivo não existir. <- Caso o arquivo existe, gera FileExistsError.
a -> Abre para escrita, e se o arquivo existir, ele escreve no final da linha.
+ -> Abre para o modo de atualização: Leitura e Escrita.

http://docs.python.org/3/library/functions.html#open


# Exemplo x
try:
    with open("university.txt", "x") as arquivo:
        arquivo.write("Teste de conteúdo.\n")
except FileExistsError:
    print("Arquivo já existe!")


# Exemplo a
with open("frutas.txt", "a") as arquivo:
    while True:
        fruta = input("Informe uma fruta ou sair: ")
        if fruta.lower() != "sair":
            arquivo.write(fruta + "\n")
        else:
            break
"""

with open("outro.txt", "r+") as arquivo:
    arquivo.write("No topo!\n")
    arquivo.write("Nova linha\n")
    arquivo.write("Mais uma linha\n")
