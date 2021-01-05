"""
Leitura de Arquivos

# OBS: Quando abrimos um arquivo com a função open(), é criado uma conexão entre o arquivo no disco do computador e o
# nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com os arquivos, devemos fechar essa
# conexão. Para isso utilizamos a função close().

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada "open()", que literalmente significa "abrir".

open() ->  Na forma mais simples de utilização, nós passamos apenas um parâmetro de entrada, que nesse caso é o
nome/diretório do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos.

Documentação -> https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo apenas para leitura. Não pode ser modificado. O arquivo deve existir!

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
mode r -> Modo de Leitura. r -> read() -> ler

"""

# Exemplo
arquivo = open("texto.txt")
# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read(). Ela lê todo o arquivo
print(arquivo.read())
# OBS: O Python utiliza um recurso para trabalhar com arquivos chamado "cursor". Esse cursor, funciona como o cursor,
# quando estamos escrevendo. Se pedir para ler o arquivo com read(), é necessário primeiro levar o cursor para o começo,
# para então poder ler novamente.
