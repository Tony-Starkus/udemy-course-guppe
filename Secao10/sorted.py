"""
Sorted
- Serve para ordernar
- Podemos utilizar o sorted com qualquer iterável.
- Sempre retorna uma Lista com os elementos do iterável ordenados

OBS: Não confuda com a função 'sort()' que já estudamos em Listas. O sort() funciona em listas.


# Exemplo
lista = [4, 7, 3, 8, 1, 4, 2]
print(lista)
lista.sort()
print(lista)

tupla = (4, 7, 3, 8, 1, 4, 2)
print(sorted(tupla))  # A alterção do sorted() não é permanente


numeros = {6, 1, 8, 2}
print(f'Original: {numeros}')
# Adicionando parâmetros ao sorted()
print(f'Ordenado: {sorted(numeros)}')
print(f'Reverso: {sorted(numeros, reverse=True)}')  # Ordena do maior para o menor


# Podemos utilizar o sorted() para coisas mais complexas
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["username"]))  # Ordenando pelo nome do usuario
print(sorted(usuarios, key=lambda usuario: usuario["tweets"]))  # Ordenando pelos tweets
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

"""

# Último exemplo
musicas = [
    {"Titulo": "Thuderstruck", "tocou": 3},
    {"Titulo": "Dead Skin Mask", "tocou": 2},
    {"Titulo": "Back in Black", "tocou": 4},
    {"Titulo": "Too old to rock'in'roll", "tocou": 32}
]

print(sorted(musicas, key=lambda musica: musica['tocou']))
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
