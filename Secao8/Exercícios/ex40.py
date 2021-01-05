def total_pares(lista):
    return sum([x for x in lista if x % 2 == 0])


print(total_pares([1, 2, 3, 4]))
