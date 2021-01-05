"""
Type Hiting

def nome_funcao(param: tipo_da_variavel) -> tipo_do_retorno


def cumprimentar(nome: str) -> str:
    return f"Olá, {nome}"


print(cumprimentar("Geek"))
"""


def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, "#")


def cabecalho1(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, "#")


print(cabecalho1("geek university"))
print(cabecalho1("geek university", False))
