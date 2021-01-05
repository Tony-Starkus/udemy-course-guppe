vogal = ['a', 'e', 'i', 'o', 'u']
with open("arq.txt") as file:
    vogais = 0
    consoantes = 0
    for line in file:
        for letter in line:
            if letter in vogal:
                vogais = vogais + 1
            else:
                consoantes = consoantes + 1
    print(f"Vogais: {vogais}")
    print(f"Consoantes: {consoantes}")

