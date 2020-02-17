"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção;

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)  # Calcular a média: somar os valores e dividir pela quantidade de elementos

# OBS: A filter() recebe dois parâmetros: uma função e um iterável
res = filter(lambda x: x > media, dados)
print(list(res))
# OBS: Após serem utilizados os dados de filter(), eles esão excluídos da memória

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises)
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
# res = filter(lambda pais: pais != '', paises)
print(list(res))


# Exemplo mais complexo:
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

"""

# A diferença entre map() e filter() é:

# map(funcao, iteravel) -> Recebe dois parâmetros e retorna um objeto mapeando a funcao para cada elemento do iteravel.

# filter(funcao, iteravel) -> Retorna um objeto filtrando apenas os elementos de acordo com a funcao.

# A função do filter() retorna True ou False indicando o valor a ser selecionado, e a função map() retorna valores.

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos combinar uma lista contendo 'Sua instrutora é ' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
