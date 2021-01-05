import os

file1 = input("Informe o path do primeiro arquivo: ")
file2 = input("Informe o path do segundo arquivo: ")

with open(os.path.splitext(file1)[0] + "_" + file2, "w") as new_file:
    with open(file1) as file:
        for line in file.readlines():
            new_file.write(line)
    with open(file2) as file:
        for line in file.readlines():
            new_file.write(line)
