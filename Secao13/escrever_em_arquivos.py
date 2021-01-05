"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler. Da mesma forma, se abrirmos um
# arquivo para escrita, não podemos lê-lo, somente escrever nele.

Para escrevermos dados em um arquivo, após abrir o arquivo, utilizamos a função write(). Esta função uma string como
parâmetro, caso contrário, teremos um TypeError.

Abrindo um arquivo para escrita como modo 'w', se o arquivo não existir, será criado. Caso ele já exista, o anterior
será apagado, e um novo será criado. Dessa forma, todo o conteudo no arquivo anterior é perdido.
"""

# Exemplo de escrita - modo 'w' - write (escrita)
with open("novo.txt", "w") as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek\n' * 1000)

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite sair: ")
        if fruta.lower() != "sair":
            arquivo.write(fruta)
        else:
            break
        arquivo.write("\n")
