with open("arq.txt") as file:
    aux = input("Qual caractere procurar?: ")
    qtd = 0
    for line in file:
        for letter in line:
            if letter == aux:
                qtd = qtd + 1
    print(qtd)
