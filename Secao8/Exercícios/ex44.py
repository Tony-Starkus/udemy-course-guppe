def funcao(x, a, b):
    a = [i for i in x if i % 2 == 0]
    b = [i for i in x if i % 2 == 1]
    return a, b


print(funcao([x for x in range(30)], [], []))
