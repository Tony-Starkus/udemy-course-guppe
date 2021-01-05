def fatorial(n):
    d = 1
    for i in range(n, 1, -1):
        d = d * i
    factorial = 1
    n = 2 * n
    for i in range(n, 1, -1):
        factorial = factorial * i
    return factorial / d


print(fatorial(3))
