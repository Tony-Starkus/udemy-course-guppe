"""
Normal: int, str, float, list, set, dict.

def dobro(valor: int) -> int:
    return valor * 2

print(dobro(8))
print(dobro(42))


Precisos:

- Literal type
# Essa função retorna uma string, que só pode ser um dos valores passados no Literal[]
def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass

def calcula(operacao: Literal['+', '-'], num1, num2):
    if operacao == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        raise ValueError(f"Operação inválida {operacao!r}")


- Union

def soma(num1: int, num2: int) -> Union[str, int]:
    resultado = num1 + num2
    if resultado > 50:
        return "Resultado é muito grande"
    else:
        return resultado


- Final

NOME: Final = "Geek"
print(NOME)
NOME = "University"
print(NOME)

# Usar o decorador @final em classes significa que a classe não pode ser extendida por outras.
@final
class Pessoa:
    pass


class Estudante(Pessoa):
    pass

    @final
    def estudar(self):
        print("Estou estudando...")


class Estagiario(Estudante):
    pass

    @final
    def estudar(self):
        print("Estudando e estagiando...")


- Typed Dictionaries

class CursoPython(TypedDict):
    versao: str
    atualizacao: int

geek = CursoPython(versao='3.8.5', atualizacao='2020')
print(geek)


- Protocols
"""
from typing import Literal, Union, Final, TypedDict, Protocol
from typing import final


class Curso(Protocol):  # Todo objeto que segue esse protocolo, tem que ter titulo. Essa classe não pode ser instânciada
    titulo: str


def estudar(valor: Curso) -> None:
    print(f"Estou estudando o curso {valor.titulo}")


class Venda:
    titulo = 'Oi'
    pass


v1 = Venda()
estudar(v1)
