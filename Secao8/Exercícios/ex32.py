def simplifica(n, d):
    for i in range(2, 11):
        while n % i == 0 and d % i == 0:
            n = n / i
            d = d / i
    return n, d


print(simplifica(36, 60))
