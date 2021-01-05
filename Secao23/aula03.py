"""
Duck Type
"""


class CisneNegro:

    def __len__(self):
        return 42


livro = CisneNegro()
print(len(livro))

nome = 'Geek University'
print(len(nome))

lista = [12, 34, 55, 49]
print(len(lista))

dicio = {"carlos": 12, "vanessa": 34, "joana": 49}
print(len(dicio))

idade = 42
print(len(idade))

peso = 81.4
print(len(peso))
