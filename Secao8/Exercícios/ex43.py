from random import randint


def funcao(x):
    while len(x) < 10:
        aux = randint(0, 1000)
        if aux not in x:
            x.append(aux)
    return x


print(funcao([]))
