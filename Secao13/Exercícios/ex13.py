with open("ex13_dados.txt", "w") as file:
    while True:
        dados = input("Informe o nome e telefone separados por espaço (0 para encerrar): ")
        if dados == "0":
            break
        file.write(dados.split(" ")[0] + " " + dados.split(" ")[1] + "\n")
    print("Os dados foram salvos!")
