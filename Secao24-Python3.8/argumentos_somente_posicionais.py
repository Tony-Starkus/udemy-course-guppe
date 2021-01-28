"""
Argumentos Somente Posicionais

float(x=0, /) <- A barra indica que o x=0 é um parâmetro posicional.
Obs: Tudo que vier antes da barra, é posicional.

Isso significa que não podemos fazer:
valor = "67.3"
print(float(x=valor))

------------------------------------------------------------------------
def cumprimenta_v5(*, nome)
Aqui está sendo indicado que todos os params apos o * devem ser declarado nominalmente.

Ex: cumprimenta_v5(nome='Geek')
"""


# valor = "67.3"
# print(float(valor))


def cumprimenta_v1(nome):
    return f"Olá {nome}"


def cumprimenta_v2(nome, /):
    return f"Olá {nome}"


def cumprimenta_v3(nome, /, mensagem="Olá"):  # Nome é posicional, mensagem não é
    return f"{mensagem} {nome}"


def cumprimenta_v4(nome, mensagem="Olá", /):
    return f"{mensagem} {nome}"


def cumprimenta_v5(*, nome):
    return f"Olá {nome}"


def cumprimenta_v6(nome, /, mensagem1="Olá", *, mensagem2):
    return f"Olá {nome}"


print(cumprimenta_v1("Geek"))
print(cumprimenta_v1(nome="Geek"))

print(cumprimenta_v2("Geek"))
# print(cumprimenta_v2(nome="Geek"))  # TypeError

print(cumprimenta_v3("Geek"))
print(cumprimenta_v3("University", mensagem="Hello"))
print(cumprimenta_v3("Felicity", "Bem-vinda"))

print(cumprimenta_v4("Geek"))
# print(cumprimenta_v4("University", mensagem="Hello"))  # TypeError
print(cumprimenta_v4("Felicity", "Bem-vinda"))

print(cumprimenta_v5(nome="Geek"))
print(cumprimenta_v5("Geek"))
