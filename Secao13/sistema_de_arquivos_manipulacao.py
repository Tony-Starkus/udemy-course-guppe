"""
Sistema de Arquivos - Manipulação


import os
# Descobrindo se um aquivo/diretório existe
# Arquivo
print(os.path.exists('arquivo.txt'))  # Resposta: False
print(os.path.exists('frutas.txt'))  # Resposta: True

# Diretório
# Paths relativos
print(os.path.exists('geek'))  # Resposta: True
print(os.path.exists('geek/university'))  # Resposta: False

# Paths absolutos
print(os.path.exists('/home/thalisson/PycharmProjects/guppe/Secao13/geek'))  # Resposta: True



# Criando arquivos
open('arquivo-teste.txt', 'w').close()

with open('arquivo-teste2.txt', 'a') as arquivo:
    pass  # Significa que vai ignorar o bloco de código e vai continuar



# Criando arquivos com "os"
os.mknod('arquivo-teste3.txt')
os.mknod('/home/thalisson/PycharmProjects/guppe/Secao13/geek/university.txt')
# OBS 1: Se você estiver utilizando no Mac OS, pode acontecer um PermissionError.
# OBS 2: Ao usar mknod(), se o arquivo existir, vai acontecer o erro FileExistsError.



# Criando diretórios
os.mkdir('templates')
# OBS 1: Ao usar mkdir(), se o diretório existir, vai acontecer o erro FileExistsError.
# OBS 2: Se não tivermos permissão para criar o diretório, vai acontecer o erro PermissionError
# OBS 3: Não é possível criar vários diretórios de uma vez com mkdir(). Isso dá erro.

# makedirs() -> Criando vários diretórios
# Criando multipos diretórios em uma única vez.
os.makedirs('templates/geek/university')

# exist_ok -> Se o path existir, ignorar, não disparar erro.
os.makedirs('templates/geek/university', exist_ok=True)



# Renomer arquivos e diretórios
os.rename('templates', 'geek2')
# OBS: Se o diretório a ser renomeado não estiver vazio, teremos um OSError
os.rename('geek/university.txt', 'geek/university1.txt')



# Deletar arquivos
# ATENÇÃO! Tome cuidado com os comandos de deletar. Ao deletar por comando, não vai para a lixeira!
os.remove('geek.txt')  # Se o arquivo não existir, vai disparar FileNotFoundError.
# No Windows, se o arquivo a ser deletado estiver em uso, será disparado um erro.
# Se informar um diretório, será disparado o IsADirectoryError.

# Deletar diretórios
os.rmdir('geek2/geek/university')
# Se o diretório não está vazio, será disparado um OSError.
# Se o diretório não existe, será disparado um FileNotFoundError.

# Removendo uma árvore de arquivos
# $ touch arquivo{1..1000}.txt
for arquivo in os.scandir('geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

# Deletar vários diretórios
os.removedirs('geek2/outro/mais')



# Trabalhando com arquivos e diretórios temporários
import tempfile

# Estamos criando um diretório temporário e um arquivo com texto. O input() é para segurar o with, pois ao ser
# finalizado, todos os arquivos/diretórios temporários são deletados.
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()
# OBS: Possivelmente não vai funcionar no Windows, pois trabalha de forma diferente com arquivos temporários.

# Criando arquivo temporário
with tempfile.TemporaryFile() as tmp:
    # Arquivp temporário só aceita ser escrito em bits.
    tmp.write(b'Geek University\n')  # O "b" converte a string para binário.
    tmp.seek(0)
    print(tmp.read())


https://docs.python.org/3/library/os.html?highlight=os#module-os
"""
