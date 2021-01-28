"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão.
Ou seja, atribui o valor para a variável, e ao mesmo tempo essa atribução retorna o valor dessa variável

variavel := expressao

print(nome = "Geek University")  # Não funciona, pois a declaração não retorna nada.
print(nome := "Geek University")  # Funciona, pois essa declaração retorna o valor da variável.


# Python 3.7
cesta = []
fruta = input("Informe a fruta: ")
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input("Informe a fruta: ")
"""

# Python 3.8
cesta = []
while (fruta := input("Informe a fruta: ")) != "jaca":
    cesta.append(fruta)
