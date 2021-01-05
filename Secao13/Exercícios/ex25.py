contatos = dict()


def add_contato():
    while True:
        nome = input("Informe o nome: ")
        if nome in contatos:
            print("Esse contato já existe!")
        else:
            break
    while True:
        telefone = input("Informe o telefone: ")
        if len(telefone) < 7:
            print("O número de telefone é inválido!")
        else:
            break
    aniversario = input("Informe o aniversário (dia e mês), separados por barra: ")
    contatos.update({nome: [telefone, aniversario]})
    print("Contato adicionado!")


def del_contato():
    nome = input("Informe o nome do contato: ")
    if nome in contatos:
        removido = contatos.pop(nome)
        print(f"O contato {nome} foi removido: {removido}")
    else:
        print("O contato não existe!")


def find_contato():
    nome = input("Informe o nome do contato: ")
    if nome in contatos:
        print(f"{nome}: {contatos[nome]}")
    else:
        print("O contato não existe!")


def find_contato_letter():
    letter = input("Informe a letra: ")
    for key1, value1 in contatos.items():
        if key1[0] == letter:
            print(f"{key1}: {value}")


def find_aniversario():
    mes = input("Informe o mês: ")
    for key2, value2 in contatos.items():
        if value2[1].split("/")[1] == mes:
            print(f"{key2}: {value2}")


with open("ex_25.bin", "a+") as file:
    file.seek(0)
    lines = file.readlines()

    if len(lines) > 0:
        print("Arquivo encontrado. Carregando dados...")
        for item in lines:
            convertido = ""
            for i in item.split(" "):
                convertido = convertido + chr(int(i, 2))
            print(convertido)
            contatos.update({convertido.split(",")[0]: [convertido.split(",")[1], convertido.split(",")[2]]})

    while True:
        op = int(input("1. Inserir contato\n2. Remover contato\n3. Pesquisar um contato por nome\n"
                       "4. Listar todos os contatos\n5. Listar os contatos cujo nome inicia com uma letra dada\n"
                       "6. Imprimir os aniversariantes do mês\n7. Sair\nOperação: "))

        if op == 1:
            add_contato()
        elif op == 2:
            del_contato()
        elif op == 3:
            find_contato()
        elif op == 4:
            for key, value in contatos.items():
                print(f"{key}: {value}")
        elif op == 5:
            find_contato_letter()
        elif op == 6:
            find_aniversario()
        elif op == 7:
            break
        else:
            print("Operação inválida!")

    for key, value in contatos.items():
        res = f"{key},{value[0]},{value[1]}"
        res_bin = " ".join(format(ord(i), 'b') for i in res)
        file.write(res_bin + "\n")
    print("Os dados foram gravados no arquivo ex_25.bin")
