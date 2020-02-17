"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

1 - SentaxError -> Ocorre quando o Python encontra um erro de síntaxe. Ou seja, você escreveu algo que o Python
               não reconhece como parte da linguagem.

# Exemplos: SyntaxError
def funcao:
    print('Geek University')

2 - NameError -> Ocorre quando uma variável ou função não foi definida
# Exemplos: NameError
a) print(geek)

b) a = 18
if a < 10:
    msg = 'É maior que 10'
print(msg)


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado
# Exemplos: TypeError
a) print(len(5))
b) print('Geek ' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tip de dado indexado utilizando
                  um índice inválido
# Exemplos: IndexError
a) lista = ['Geek']
print(lista[2])

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto
                  mas valor inapropriado.
# Exemplos: ValueError
a) print(int('Geek'))


6 - KeyError -> Ocorre quando tentamos aessar um dicionário com uma chave que não existe.
# Exemplos: KeyError
a) dic = {}
print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.
# Exemplos: AttributeError
a) tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)


OBS: Exceptions e Erros são sinônimos na programação.
OBS: Importante ler e prestar atenção na saída de erro.
"""

