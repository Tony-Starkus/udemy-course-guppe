def fatorial(x):
    aux = 1
    for i in range(1, x + 1):
        aux = aux * i
    return aux


print(fatorial(5))
print(fatorial(4))
print(fatorial(3))
