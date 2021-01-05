with open(input("Informe o path do arquivo: ")) as file:
    palavra = input("Informa a palavra a ser encontrada: ")
    aux = 0
    for line in file.readlines():
        if line.find(palavra) != -1:
            aux = aux + 1
    print(f"Total de repetição da palavra: {aux}")
