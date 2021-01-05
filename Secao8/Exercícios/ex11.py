def calcular(n1, n2, n3, op):
    if op.lower() == 'a':
        return (n1 + n2 + n3) / 3
    elif op.lower() == 'p':
        return ((n1*5) + (n2*3) + (n3*2)) / (5 + 3 + 2)
    else:
        return "Operação Inválida!"


aux = input("Informe as 3 notas e a operação, serapados por espaço: ").split(" ")
resultado = calcular(int(aux[0]), int(aux[1]), int(aux[2]), aux[3])
print(resultado)
