"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}


receita = {'jan': 100, 'fev': 250, 'mar': 400}
# Iterar sobre dicionários
for chave in receita:
    print(chave)  # Imprime o valor da chave

for chave in receita:
    print(receita[chave])  # Imprime o valor da chave

for chave in receita:
    print(f'{chave} : {receita[chave]}')

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')


print(receita.keys())  # Imprimindo as chaves.
print(receita.values())  # Imprimindo os valores.

for valor in receita.values():
    print(valor)

# Modo pythônico
for chave in receita.keys():
    print(receita[chave])


# Desempacotamento de dicionários
print(receita.items())  # Mostra uma lista contendo tupla da chave e valor
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiro ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""
