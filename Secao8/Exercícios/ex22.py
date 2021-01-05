def funcao(n):
    for i in range(n):
        result = "!"
        for j in range(i):
            result = result + "!"
        print(result)


funcao(5)
