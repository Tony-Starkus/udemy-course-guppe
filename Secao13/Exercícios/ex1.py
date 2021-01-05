with open("arq.txt", "w") as file:
    while True:
        aux = input("Digite algo: ")
        if aux == "0":
            break
        file.write(f"{aux}\n")

with open("arq.txt") as file:
    for line in file:
        print(line)
