def funcao(n):
    result = 0
    for i in range(1, n + 1):
        result = result + ((n**2 + 1)/(n+3))
    return result


print(funcao(5))
