from random import choice, randint

# preguiça também


def media_idade(p1, p2, p3, p4, p5):
    return sum([p1[3], p2[3], p3[3], p4[3], p5[3]]) / 5


# p = [sexo, cor_dos_olhos, cor_dos_cabelos, idade]
sexo = ["M", "F"]
cor_olhos = ["A", "C"]
cor_cabelos = ["L", "P", "C"]
p1 = [choice(sexo), choice(cor_olhos), choice(cor_cabelos), randint(0, 91)]
p2 = [choice(sexo), choice(cor_olhos), choice(cor_cabelos), randint(0, 91)]
p3 = [choice(sexo), choice(cor_olhos), choice(cor_cabelos), randint(0, 91)]
p4 = [choice(sexo), choice(cor_olhos), choice(cor_cabelos), randint(0, 91)]
p5 = [choice(sexo), choice(cor_olhos), choice(cor_cabelos), randint(0, 91)]

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
