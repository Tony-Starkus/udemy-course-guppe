from random import random


def create_file():
    with open("ex18_entrada.txt", "w") as file:
        products = ["Playstation 4", "Xbox 360", "Notebook Samsung X40", "iPhone X", "Mouse", "Headset JBL"]
        for item in products:
            file.write(f"{item}: {round(random() * 1000, 2)}\n")


# Criar arquivo de entrada
# create_file()

with open("ex18_entrada.txt") as file1:
    pay = 0
    for line in file1:
        pay = pay + float(line.split(":")[1])
    print(f"Total a pagar: R$ {round(pay, 2)}")
