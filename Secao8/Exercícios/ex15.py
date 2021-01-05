def lado_triangulo():
    x = float(input("Informe o valor: "))
    if x <= 0:
        print("O valor não pode ser zero!")
        exit()
    if x.is_integer():
        return int(x)
    return x


def confirmar_triangulo(x1, x2, x3):
    if x1 >= x2 + x3:
        return "Não forma um triângulo!"
    elif x2 >= x1 + x3:
        return "Não forma um triângulo!"
    elif x3 >= x1 + x2:
        return "Não forma um triângulo!"

    if x1 == x2 == x3:
        return "Triângulo Equilátero"
    elif x1 == x2 or x1 == x3 or x2 == x3:
        return "Triângulo Isósceles"
    elif x1 != x2 != x3:
        return "Triângulo Escaleno"


l1 = lado_triangulo()
l2 = lado_triangulo()
l3 = lado_triangulo()
result = confirmar_triangulo(l1, l2, l3)
print(result)
