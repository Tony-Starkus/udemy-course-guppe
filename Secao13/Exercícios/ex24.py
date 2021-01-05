produtos = dict()


def add_produto():
    id_produto = -1
    while True:
        id_produto = int(input("Informe o ID do produto: "))
        if id_produto in produtos:
            print("O ID já existe!")
        elif id_produto < 0:
            print("O ID não pode ser negativo!")
        else:
            break
    descricao_produto = input("Informe uma descrição para o produto: ")
    while True:
        estoque_produto = int(input("Informe a quatidade do produto: "))
        if estoque_produto < 0:
            print("O estoque não pode ser menor que zero!")
        else:
            break
    produtos.update({id_produto: [descricao_produto, estoque_produto]})
    print("O produto foi armazenado!")


def del_produto():
    for item1, value1 in produtos.items():
        print(f"{item1}: {value1[0]}")

    while True:
        produto = int(input("Informe o ID do produto que deseja retirar: "))
        if produto in produtos:
            break
        else:
            print("O ID não existe!")

    while True:
        retirar = int(input("Informe quanto deseja retirar do estoque: "))
        if retirar > produtos[produto][1]:
            print("Você está tentando tirar mais do que tem no estoque!")
        else:
            produtos.update({produto: [produtos[produto][0], produtos[produto][1] - retirar]})
            print("Concluído!")
            break


with open("ex24_dados.bin", "w") as file:

    while True:
        op = int(input("1. Listar Produtos\n2. Adicionar Produto\n3. Retirar Produto\n4. Sair\n"))

        if op == 1:
            for item, value in produtos.items():
                print(f"{item}: {value}")
        elif op == 2:
            add_produto()
        elif op == 3:
            del_produto()
        elif op == 4:
            break
        else:
            print("Operação Inválida!")
    print("Salvando dados")
    for item, value in produtos.items():
        res = f"{item}: {value[0]}, {value[1]}"
        res_bin = ' '.join(format(ord(i), 'b') for i in res)
        file.write(res_bin + "\n")
    print("Done!")
