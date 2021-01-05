vogais = ['a', 'e', 'i', 'o', 'u']
with open('arq.txt') as file:
    linhas = file.readlines()
    new_file = []
    for linha in linhas:
        for vogal in vogais:
            linha = linha.replace(vogal, "*")
        new_file.append(linha)
    print(new_file)
    with open("arq2.txt", "w") as file2:
        for line in new_file:
            file2.write(line)
