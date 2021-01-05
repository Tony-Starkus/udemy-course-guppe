"""
Debugando com PDB
PDB -> Python Debugger

# Exemplo com o PyCharm


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as error:
        return f"Ocorreu um problema: {error}"


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando do debbuger.
# Em Python, podemos fazer isso em diferentes IDE's, como o PyCharm ou utilizando o PDB - Python Begguger

# Exemplo com o PDB - Python Debbuger
# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
import pdb
# * -> A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in (integrada) chamada breakpoint().

# Comandos básicos do pdb
# l -> Listar onde estamos no código
# n -> Próxima linha
# p -> Imprime variável
# c -> Continua a execução - finaliza o debbuging
# <nome_variável> -> Vai mostrar o valor de uma variável (sem <>)

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + "  faz o curso " + curso
print(final)


"""

# Existem formas mais profissionais de se fazer esse 'debug', utilizando do debbuger.
# Em Python, podemos fazer isso em diferentes IDE's, como o PyCharm ou utilizando o PDB - Python Begguger

# Comandos básicos do pdb
# l -> Listar onde estamos no código
# n -> Próxima linha
# p -> Imprime variável
# c -> Continua a execução - finaliza o debbuging
# <nome_variável> -> Vai mostrar o valor de uma variável (sem <>)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
# Por que utilizar esse formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no início do arquivo. Por isso, ao invés de colocarmos o import no início do arquivos,
# nós colocamos somente onde vamos debbugar, e ao finalizar já fazemos a remoção.
nome_completo = nome + ' ' + sobrenome
breakpoint()  # A partir do Python 3.7
curso = "Programação em Python: Essencial"
final = nome_completo + "  faz o curso " + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb
# Por exemplo, uma variável chamada 'l' vai dar problema ao tentar usar o comando 'l' no pdb.
