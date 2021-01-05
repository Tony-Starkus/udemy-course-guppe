import numpy as np

matriz = np.arange(1, 401).reshape(20, 20)
maior = []

for i in range(20):
    for j in range(20):
        num0 = matriz[i, j]
        for k in range(5):
            if k == 0:  # Diagonal para baixo
                num1 = matriz[i + 1, j + 1] if i + 1 < 20 and j + 1 < 20 else 0
                num2 = matriz[i + 2, j + 2] if i + 2 < 20 and j + 2 < 20 else 0
                num3 = matriz[i + 3, j + 3] if i + 3 < 20 and j + 3 < 20 else 0
                if sum([num0, num1, num2, num3]) > sum(maior):
                    maior.clear()
                    maior = [num0, num1, num2, num3]
            elif k == 1:  # Direita
                num1 = matriz[i, j + 1] if j + 1 < 20 else 0
                num2 = matriz[i, j + 2] if j + 2 < 20 else 0
                num3 = matriz[i, j + 3] if j + 3 < 20 else 0
                if sum([num0, num1, num2, num3]) > sum(maior):
                    maior.clear()
                    maior = [num0, num1, num2, num3]
            elif k == 2:  # Esquerda
                num1 = matriz[i, j - 1] if j - 1 > -1 else 0
                num2 = matriz[i, j - 2] if j - 2 > -1 else 0
                num3 = matriz[i, j - 3] if j - 3 > -1 else 0
                if sum([num0, num1, num2, num3]) > sum(maior):
                    maior.clear()
                    maior = [num0, num1, num2, num3]
            elif k == 3:  # Cima
                num1 = matriz[i - 1, j] if i - 1 > -1 else 0
                num2 = matriz[i - 2, j] if i - 2 > -1 else 0
                num3 = matriz[i - 3, j] if i - 3 > -1 else 0
                if sum([num0, num1, num2, num3]) > sum(maior):
                    maior.clear()
                    maior = [num0, num1, num2, num3]
            elif k == 4:  # Baixo
                num1 = matriz[i + 1, j] if i + 1 < 20 else 0
                num2 = matriz[i + 2, j] if i + 2 < 20 else 0
                num3 = matriz[i + 3, j] if i + 3 < 20 else 0
                if sum([num0, num1, num2, num3]) > sum(maior):
                    maior.clear()
                    maior = [num0, num1, num2, num3]

print(maior)
