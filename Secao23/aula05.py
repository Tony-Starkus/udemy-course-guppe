"""
Checagem de tipos com MyPy
"""


def cabecalho1(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, "#")


print(cabecalho1("geek university"))
print(cabecalho1("geek university", False))
# print(cabecalho1("aaa", alinhamento="eita"))
