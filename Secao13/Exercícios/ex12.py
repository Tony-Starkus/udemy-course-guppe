
with open("arq_arq2.txt") as file:
    qtd_lines = len(file.readlines())
    qtd_words = 0
    qtd_letters = dict()
    file.seek(0)
    for line in file.readlines():
        qtd_words = qtd_words + len(line.split(" "))
        for letter in line:
            if letter in qtd_letters:
                qtd_letters.update({letter: qtd_letters[letter] + 1})
            else:
                qtd_letters.update({letter: 1})

    print(f"Total de lines: {qtd_lines}")
    print(f"Total de palavras: {qtd_words}")
    print(f"Total de letras:{qtd_letters}")
