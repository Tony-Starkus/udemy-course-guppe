
with open("ex14_dados.txt") as file1:
    with open("ex28.txt", "w") as file2:
        for line in file1.readlines():
            file2.write(line[::-1])
