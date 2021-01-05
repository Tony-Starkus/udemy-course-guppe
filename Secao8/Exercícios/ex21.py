def total_primos(n):
    result = []
    for i in range(2, n):
        primo = True
        for j in range(2, i):
            print(i, j)
            if i % j == 0:
                primo = False
                break
        if primo:
            result.append(i)
    return result


print(total_primos(6))
print(total_primos(41))
