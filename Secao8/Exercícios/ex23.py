def funcao(n):
    for i in range(n):
        result = "*"
        for j in range(i):
            result = result + "*"
        print(result)

    for i in range(n - 1, 0, -1):
        result = ""
        for j in range(i):
            result = result + "*"
        print(result)


funcao(4)
