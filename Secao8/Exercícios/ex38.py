from math import factorial


def fatorial_exponencial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * factorial(i)
    print(n ** result)


fatorial_exponencial(2)
