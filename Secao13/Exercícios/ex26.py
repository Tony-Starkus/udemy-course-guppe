class Aluno:
    matricula = None
    sobrenome = None
    ano_nascimento = None


dados = list()
with open("ex26_dados.txt", "w") as file:
    while True:
        op = int(input("1. Inserir aluno\n2. Sair\nOperação: "))
        if op == 1:
            aluno = Aluno()
            aluno.matricula = int(input("Informe o número de matrícula: "))
            aluno.sobrenome = input("Informe o sobrenome: ")
            aluno.ano_nascimento = int(input("Informe o ano de nascimento: "))
            dados.append(aluno)
        elif op == 2:
            break
        else:
            print("Operação inválida!")

    for aluno in dados:
        file.write(f"{aluno.matricula},{aluno.sobrenome},{aluno.ano_nascimento}\n")
    print("Done!")
