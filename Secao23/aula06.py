"""
Annotations

# OBS: Objetos não tem __annotations__, apenas funções.

# Correto
alinhamento: bool = True

# Incorreto
alinhamento : bool = True
alinhamento:bool=True
alinhamento: bool=True


# Correto
texto: str

# Incorreto
texto:str
texto : str


# Correto
def function() -> str:

# Incorreto
def function()->str:
def function()-> str:
"""


def cabecalho1(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, "#")


print(cabecalho1("geek university"))
print(cabecalho1("geek university", False))
print(cabecalho1.__annotations__)
# print(cabecalho1("aaa", alinhamento="eita"))


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso = peso

    def andar(self) -> str:
        return f"{self.__nome} está andando"


p = Pessoa("Geek University", 37, 69.5)
print(p.__dict__)
print(p.andar())
print(p.andar.__annotations__)
# print(p.__annotations__)
