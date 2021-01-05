"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')

print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek().
# A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos
# colocar o cursor.
arquivo.seek(0)

print(arquivo.read())

"""

arquivo = open('texto.txt')

# Lê o arquivo linha por linha.
print(arquivo.readline())  # linha 1
print(arquivo.readline())  # linha 2
print(arquivo.readline())  # linha 3

# readlines() -> Retorna uma lista, onde cada linha é colocada como um item na lista.
arquivo.seek(0)
print(arquivo.readlines())
print(arquivo.closed)  # Verifica se o arquivo está fechado. True para fechado e False para aberto.
