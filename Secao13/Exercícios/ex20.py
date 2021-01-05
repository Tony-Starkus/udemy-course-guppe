from names import get_full_name
from random import randint


def create_data(v1, v2):
    for i in range(15):
        name = get_full_name()
        if len(name) < 40:
            name = name + (" " * (40 - len(name)))
        v1.append(name)
        v2.append(randint(0, 10))


vector_names = list()
vector_grades = list()
create_data(vector_names, vector_grades)

with open("ex20_dados.txt", "w") as file:
    for name, grade in zip(vector_names, vector_grades):
        file.write(f"NOME: {name} NOTA: {grade}\n")
print("Done!")
