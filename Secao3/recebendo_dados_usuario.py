"""
Recebendo dados do usuário

input -> Todo dado recebido via input é do tipo String

"""
# Entrada de dados

# print("Qual seu nome?")
# nome = input()  # Input -> Entrada

nome = input("Qual seu nome? ")

# Exemplo de print 'antigo' 2.x
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print("Seja bem-vindo(a) {0}" .format(nome))

# Exemplo de print 'mais atual' 3.6+
print(f"Seja bem-vindo(a) {nome}")

# print("Qual sua idade")
# idade = input()

idade = int(input("Qual sua idade? "))

# Processamento

# Saída
# print('O %s tem %s anos' % (nome, idade))
# print("O {0} tem {1} anos" .format(nome, idade))

print(f"O {nome} tem {idade} anos")

"""
int(idade) -> cast
Cast é a 'conversão' de um tipo de dado para outro
"""

# print(f"O {nome} nasceu em {2018 - int(idade)}")
print(f"O {nome} nasceu em {2018 - idade}")
