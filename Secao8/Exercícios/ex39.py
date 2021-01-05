def troque(a, b):
    aux = a
    a = b
    b = aux
    return {'a': a, 'b': b}


print(troque(5, 10))
