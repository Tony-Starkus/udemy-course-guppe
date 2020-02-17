"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por 'Mapas'.

Dicionários são coleções do tipo chave/valor.
[0, 1, 2] <- chave/index
[1, 2, 3] <- valor

Dicionários são representados por chaves {}

OBS: Sobre dicionários
    - Chave e Valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;



# Criação de dicionários

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)


# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
# OBS: Caso tentar utilizar uma chave que não existe, vai dar erro.

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('ru'))  # Vai retornar 'None'




pais = paises.get('ru')  # Se o get não encontrar, o valor vai ser None. Isso não gera erro.
# O tipo None é 'Falso'.
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

pais = paises.get('ru', 'Não encontrado')  # Procurar chave 'ru'. Se não encontrar, receber valor do segundo parâmetro.




# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)  # True
print('ru' in paises)  # False
print('Estados Unidos' in paises)  # False

if 'ru' in paises:
    russia = paises['ru']




# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla dicionario, como chaves
# de dicionários
# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas
# são imutáveis.
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 112.4194): 'Escritório em São Paulo',
}
print(localidades)
print(type(localidades))




# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)  # Outra forma -> receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)
# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.




# Remover dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
# Forma 1 - Mais comum
print(receita)
ret = receita.pop('mar')
print(receita)
print(ret)
# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao remover um objeto, o valor deste objeto é sempre retornada.

# Forma 2
del receita['fev']
print(receita)
# del receita['fev'] -> Se a chave não existir, vai dar erro. Neste caso o valor removido não é retornado.

"""
print(type({}))  # print: <class 'dict'>

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho dde Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    
    Produto 2:
        - nome;
        - quantidade;
        - preço;

# 1 - Poderiamos utilizar uma Lista para isso? Sim!
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto.


# 2 - Poderiamos utilizar uma Tupla para isso? Sim!
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto.


# 3 - Poderiamos utilizar um dicionário para isso? Sim!
carrinho = []  # Essa lista vai receber Dicionário :)
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}  # Dicionário
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}  # Dicionário
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação





# Métodos de dicionários.
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário
d.clear()
print(d)

# Copiando um dicionário para outro
# Forma 1 - Deep Copy
novo = d.copy()
print(novo)
novo['d'] = 4  # Deep Copy
print(d)
print(novo)  # Nesse caso, o dicionário d fica imutável, pois o novo não utiliza o mesmo endereço do d.

# Forma 2 - Shallow Copy
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)
"""
# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')  # .fromkeys(chave, valor)
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(outro))
# O método .fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')  # Não vai usar as duas ultimas letras, pois elas se repetem no começo.
print(veja)
veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
