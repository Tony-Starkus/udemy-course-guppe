"""
Listas Aninhadas (Nested Lists)

-Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionai (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as Listas
numeros = [1, 'b', 3.234, True, 5]
"""

# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3 | Cada lista é linha, cada valor dentro das listas é coluna.

# Como fazemos para acessar os dados
print(listas[0])  # Output: [1, 2, 3]
print(listas[0][1])  # Output: 2 | listas[linha][coluna]

# Iterando com loops em uma lista aninhada
for linha in listas:
    for coluna in linha:
        print(coluna, end=" ")
    print()

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos

# Gerando um tabuleiro/matrix 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
