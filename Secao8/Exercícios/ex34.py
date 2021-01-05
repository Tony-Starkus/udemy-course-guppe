def fatorial(n):
    factorial = 1
    for i in range(n, 1, -1):
        if i % 2 == 1:
            factorial = factorial * i
    return factorial


print(fatorial(4))
