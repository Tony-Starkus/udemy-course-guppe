from random import randint

with open("ex10_entrada.txt", "w") as file:
    for i in range(10):
        file.write(f"Cidade {i}: {randint(1, 100000)}\n")

with open("ex10_saida.txt", "w") as file:
    dicionario = dict()
    file_entrada = open("ex10_entrada.txt")
    entrada = file_entrada.readlines()
    file_entrada.close()
    for i in entrada:
        dicionario.update({i.split(":")[0]: int(i.split(":")[1])})
    file.write(f"{max(dicionario, key=dicionario.get)}: {dicionario[max(dicionario, key=dicionario.get)]}")
