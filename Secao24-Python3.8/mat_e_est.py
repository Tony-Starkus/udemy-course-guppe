"""

## MATH
import math

# mat.prod - retorna o produto de um container numérico.
Container numérico é um array de numeros, seja list, set ou tupla.

nums_v1 = [2, 3, 6, 8]
nums_v2 = (2, 3, 6, 8)
nums_v3 = {2, 3, 6, 8}
print(math.prod(nums_v1))  # 2 * 3 * 6 * 8 = 288
print(math.prod(nums_v2))  # 2 * 3 * 6 * 8 = 288
print(math.prod(nums_v3))  # 2 * 3 * 6 * 8 = 288


# math.isqrt - retorna a raiz quadrada do número informado, mas o retorno é inteiro (não arredonda).

print(math.isqrt(9))  # 3
print(math.sqrt(9))  # 3.0
print(math.isqrt(17))  # 4
print(math.sqrt(17))  # 4.123105625617661


# math.dist - retorna a distância euclidiana entre dois pontos, seja 2D ou 3D.

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)
# Pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]
print(f'{math.dist(p3d1, p3d2) = }')
print(f'{math.dist(p2d1, p2d2) = }')


# math.hypot - retorna a hipotenusa, ou a norma Euclidiana.

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)
print(f'{math.hypot(*p3d1) = }')
print(f'{math.hypot(*p3d2) = }')


## STATISTICS
import statistics

# statistics.fmean - calcula a média de números reais.

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]
print(f"{statistics.fmean(valores_reais) = }")
print(f"{statistics.fmean(valores_inteiros) = }")


# statistics.geometric_mean - calcula a média geométrica de números reais.

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]
print(f"{statistics.geometric_mean(valores_reais) = }")
print(f"{statistics.geometric_mean(valores_inteiros) = }")


# statistics.multimode - retorna o valor mais frequente em uma sequência.

seq1 = 'Geek University'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]
print(f"{statistics.multimode(seq1) = }")
print(f"{statistics.multimode(seq2) = }")
print(f"{statistics.multimode(seq3) = }")
"""
import statistics

seq1 = 'Geek University'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]
print(f"{statistics.multimode(seq1) = }")
print(f"{statistics.multimode(seq2) = }")
print(f"{statistics.multimode(seq3) = }")
