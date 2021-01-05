vogal = ['a', 'e', 'i', 'o', 'u']
with open("arq.txt") as file:
    aux = 0
    for line in file:
        for letter in line:
            if letter in vogal:
                aux = aux + 1
    print(aux)
