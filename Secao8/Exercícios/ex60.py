def posicao(x, y):
    if y not in x:
        return -1
    else:
        return x.find(y)


print(posicao("Hoje o dia está bom", "dia"))
