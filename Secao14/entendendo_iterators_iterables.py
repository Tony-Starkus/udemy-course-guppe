"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por ver quando uma função next() é chamada;

Iterable ->
    - Um objeto que vai retornar um iterator quando a função iter() for chamada.



nome = 'Geek'  # É um iterable, mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable, mas não é um interator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print()

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

"""

nome = 'Geek'  # É um iterable, mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable, mas não é um interator
