"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazeno referência à Teoria dos Conjuntos da matemática

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valore ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles.
Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos(Sets) e Mapas(Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;



# Definindo um conjunto
# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.
print(s)  # OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem erros.
print(type(s))

# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')



# Importante lembrar que, além e não termos valores duplicados, não temos ordem
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]  # Lista aceitam valores duplicados, então temos 10 elementos.
print(f'Lista: {lista} com {len(lista)} elementos')
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)  # Lista aceitam valores duplicados, então temos 10 elementos.
print(f'Tupla: {tupla} com {len(tupla)} elementos')
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')  # Apenas 8 elementos, não aceita chave duplicada
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}  # Apenas 8 elementos, não aceita valor duplicado
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')



# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um Set normalmente
for valor in s:
    print(valor)




# Usos interessantes com Set
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu.
# E os visitantes informam manualmente a cidade de onde vieram.
# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades))
# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
print(len(set(cidades)))



# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)




# Remover elementos em um conjunto
s = {1, 2, 3}
s.remove(3)  # Forma 1 | Não é índice, é o valor.
# OBS: Caso o valor não seja encontrado, será gerado erro, usando o .remove()
print(s)
s.discard(2)  # Forma 2
# OBS: Caso o valor não seja encontrado, não vai gerar erro, usando o .discard()
print(s)



# Copiando um conjunto para outro...
s = {1, 2, 3}
# Forma 1 - Deep Copy
novo = s.copy()
novo.add(4)
print(novo)
print(s)
# Forma 2 - Shallow Copy
novo = s
novo.add(4)
print(novo)
print(s)




# Podemos remover todos os itens de um conjunto
s = {1, 2, 3}
s.clear()
print(s)




# Métodos Matemáticos de Conjuntos
# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes do curso Java.
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
# Veja que alguns alunos que estudam Python, também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos.
# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
# Forma 2 - Utilizando o caractere pipe -> | <-
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar conjunto de estudantes que estão em ambos os cursos
# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)
# Forma 2 -- Utilizando -> & <-
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar estudantes de um curso que não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
