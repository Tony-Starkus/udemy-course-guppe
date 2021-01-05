file_name = input("Informe o path do arquivo: ")

with open(file_name) as file:
    with open("new_" + file_name, "w") as new_file:
        for line in file:
            new_file.write(line.title())
