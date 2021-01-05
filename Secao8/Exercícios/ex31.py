from math import factorial


def deperiano(n):
    result = 0
    for i in range(n):
        result = result + (1/factorial(n))
    return result


print(deperiano(4))
