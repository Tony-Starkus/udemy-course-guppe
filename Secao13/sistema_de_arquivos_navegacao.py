"""
Sistemas de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistemas operacional, precisamos importar e fazer uso do módulo "os".

OS -> Operating System - Sistema Operacional


import os

# getcwd() -> get current work directory - Pega o diretório absoluto atual.
print(os.getcwd())  # Resposta: /home/thalisson/PycharmProjects/guppe/Secao13

# chdir -> change directory - Mudar de diretório.
os.chdir('..')
print(os.getcwd())  # Resposta: /home/thalisson/PycharmProjects/guppe

# os.path.isabs('<directory>') -> Podemos chegar se um diretório é absoluto ou relativo.
print(os.path.isabs('/home/geek'))  # Resposta: True

# OBS para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com Windows, terá que ter cuidado ao verificar diretórios.

# Podemos identificar o sistema operacional com o módulo os.
# posix (Linux e Mac) | nt (Windows)
print(os.name)  # Resposta: posix

# Podemos ter mais detalhes no sistema operacional
print(os.uname())



import sys

print(sys.platform)  # Resposta: linux



# Criando diretório
print(os.getcwd())
res = os.path.join(os.getcwd(), 'geek')  # Pode passar N strings, cada uma representando uma pasta/diretório
os.chdir(res)
print(os.getcwd())

# listdir() -> Podemos listar os arquivos/diretórios
print(os.listdir())  # Retona uma uma lista de strings onde cada arquivo/pasta do diretório atual está dentro da lista.
"""
import os

# scandir() -> Podemos listar os arquivos e diretórios com mais detalhes.
scanner = os.scandir()
arquivos = list(scanner)
print(arquivos)
print(dir(arquivos[0]))
print(arquivos[0].name)  # Nome
print(arquivos[0].is_dir())  # É um diretório?
print(arquivos[0].is_file())  # É um arquivo?
print(arquivos[0].path)  # Caminho relativo

# OBS: quando utilizamos a função scandir(), nós precisamos fechá-la
scanner.close()
