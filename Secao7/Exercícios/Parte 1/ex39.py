def triangulopascal(n):
    lista = [[1], [1, 1]]
    for i in range(1, int(n)):
        linha = [1]
        for j in range(0, len(lista[i]) - 1):
            linha += [lista[i][j] + lista[i][j + 1]]
        linha += [1]
        lista += [linha]
    return lista


n = input("Digite o número de linhas para o triângulo de Pascal: ")
resultado = triangulopascal(n)
print(resultado)
for i in range(len(resultado)):
    print(resultado[i])
