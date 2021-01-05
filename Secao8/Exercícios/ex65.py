def concatenar(str1, str2, n):
    for i in range(n):
        if i < len(str2):
            str1 = str1 + str2[i]
    str2 = None
    return str1


print(concatenar("O dia está ", "lindo", 2))
