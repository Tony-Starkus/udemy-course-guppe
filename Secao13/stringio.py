"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória
"""
# Primeiro fazermos o import
from io import StringIO

mensagem = 'Este é apenas uma string normal'

# Podemos criar um arquivo me memória, já com uma string inserida, ou mesmo vazio, para inserirmos texto posteriormente.
arquivo = StringIO(mensagem)  # == arquivo = open('arquivo', 'w')

# Agora, tendo o arquivo, podemos utilizar todas as funções relacionadas a arquivos.
