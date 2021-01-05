import numpy as np
matriz1 = np.arange(0, 4).reshape(2, 2)
matriz2 = np.arange(5, 9).reshape(2, 2)

op = ''
while op != 'e':
    print("(a) Somar as duas matrizes\n"
          "(b) Subtrair a primeira matriz da segunda\n"
          "(c) Adicionar uma constante às duas matrizes\n"
          "(d) Imprimir as matrizes\n"
          "(e) Sair")
    op = input("Operação: ")

    if op == 'a':
        matriz = np.zeros(shape=(2, 2))
        for i in range(2):
            for j in range(2):
                matriz[i, j] = matriz1[i, j] + matriz2[i, j]
        print(matriz)
    elif op == 'b':
        matriz = np.zeros(shape=(2, 2))
        for i in range(2):
            for j in range(2):
                matriz[i, j] = matriz1[i, j] - matriz2[i, j]
        print(matriz)
    elif op == 'c':
        print("Não implementado. Questão confusa!")
    elif op == 'd':
        print(matriz1)
        print()
        print(matriz2)
    elif op == 'e':
        break
    else:
        print('Operação inválida')
