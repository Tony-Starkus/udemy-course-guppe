from random import randint

vetor = [randint(0, 999999) for x in range(10)]

with open("ex16_dados.txt", "w") as file:
    for i in vetor:
        file.write(bin(i) + "\n")
    print("Concluído")
