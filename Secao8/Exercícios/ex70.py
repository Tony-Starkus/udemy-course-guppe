# Coisa chata
def reduz(a, b):
    return f"{int(a)}/{int(b)}" if int(b) > 0 else "Denominador tem que ser maior que zero"


def neg(a, b):
    return f"-{int(a)}/-{int(b)}" if int(b) > 0 else "Denominador tem que ser maior que zero"


def soma(a, b):
    aux = int(a.split("/")[0]) + int(b.split("/")[0])
    d = a.split("/")[1]
    return f"{aux}/{d}" if d > 0 else "Denominador tem que maior ser que zero"


def mult(a, b):
    n = int(a.split("/")[0]) * int(b.split("/")[0])
    d = int(b.split("/")[1]) * int(b.split("/")[1])
    return f"{a.split('/')}" if d > 0 else "Denominador tem que ser maior que zero"

