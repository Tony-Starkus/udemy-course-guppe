
# /models/produto.py
class Produto:
    contador: int = 1

    def __init__(self, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> str:
        return self.__preco

    def __str__(self) -> str:
        return f"Código: {self.codigo}\nNome: {self.nome}\n"
# /models/produto.py


ps4: Produto = Produto("Playstation 4", 1789.44)
xbox: Produto = Produto("Xbox 360", 1699.00)

print(ps4)
print(xbox)

nome: str = input("Informe o nome do produto: ")
produto: Produto = Produto(nome, preco := int(input("Informe o preço do produto")))
print(produto.preco)

# main
from typing import List, Dict


