dicionario = {}

with open("arq.txt") as file:
    for line in file:
        for letter in line:
            if letter in dicionario:
                dicionario.update({letter: dicionario[letter] + 1})
            else:
                dicionario.update({letter: 1})
    print(dicionario)
