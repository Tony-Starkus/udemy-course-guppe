"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas onde foram declaradas, ou seja, seu escopo está
    limitado ao bloco onde foram declarada.

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel


Python é uma linagem de tipagem dinâmica. Isso significa que ao declarar uma variável, nós não colocamos
o tipo de dado dela. Esse tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C/Java:
int numero = 42;

Exemplo em Python:
numero = 42

"""

numero = 42
print(numero)
print(type(numero))

# Reatribuição
numero = 'Geek'
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10  # A variável 'novo' está declarada localmente dentro do boloc do if. Portanto, é local.
    print(novo)

print(novo)
