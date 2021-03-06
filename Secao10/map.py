"""
Map

Com map, fazemos mapeamento de valores para função.

import math

# Calcula a área de um círculo com o raio 'r'.
def area(r):
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]
# Forma comum
print("Forma comum")
areas = []
for r in raios:
    areas.append(area(r))

print(areas)
print("-----------------------------------------------------------------------------------------")
# Forma - Map
# map(funcao, iteravel) recebe dois parâmetros: o primeiro é função, o segundo é um iterável.
print("Forma - Map")
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))
print("-----------------------------------------------------------------------------------------")
# Forma - Map com Lambda
print("Forma - Map com Lambda")
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# Após utilizar a função map() depois da primeira utilização do resultado, ele zera.


"""

# Para ficar - Map

# Temos dados iteráveis:
# dados: a1, a2, ..., an

# Temos uma função:
# Função: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an)

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 26), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)
# f = 9/5 * c + 32

# Lambda
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
