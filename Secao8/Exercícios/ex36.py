from math import factorial


def superfatorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * factorial(i)
    return result


print(superfatorial(4))
