def funcao(n):
    factorial = 1
    for i in range(n, 1, -1):
        factorial = factorial * i
    result = 0
    for i in str(factorial):
        result = result + int(i)
    return result


print(funcao(4))
