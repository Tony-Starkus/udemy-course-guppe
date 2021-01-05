class Aluno:
    def __init__(self):
        self.nome = ""
        self.notas = []


turma_info = []
alunos = []


def add_aluno():
    aluno = Aluno()
    aluno.nome = input("Informe o nome do aluno: ")
    for i in range(1, 5):
        while True:
            nota = float(input(f"Informe a N{i}: "))
            if 0 <= nota <= 10:
                aluno.notas.append(nota)
                break
            else:
                print("Nota inválida! Informe um valor de 0 a 10.")
    alunos.append(aluno)


def main():
    with open("ex27_dados.txt", "w") as file:
        while True:
            op = int(input("1. Definir informações da turma\n"
                           "2. Inserir aluno e notas\n"
                           "3. Exibir alunos e média\n"
                           "4. Exibir alunos aprovados\n"
                           "5. Exibir alunos reprovados\n"
                           "6. Salvar dados em Disco\n"
                           "7. Sair do programa\n"
                           "Operação: "))

            if op == 1:
                turma_info.clear()
                turma_info.append(input("Nome da turma: "))
                turma_info.append(input("Turno: "))
            elif op == 2:
                add_aluno()
            elif op == 3:
                for aluno in alunos:
                    print(f"Nome: {aluno.nome} | Média: {sum(aluno.notas) / 4}")
            elif op == 4:
                for aluno in alunos:
                    if (sum(aluno.notas) / 4) >= 7:
                        print(f"Nome: {aluno.nome} | Média: {sum(aluno.notas) / 4}")
            elif op == 5:
                for aluno in alunos:
                    if (sum(aluno.notas) / 4) < 7:
                        print(f"Nome: {aluno.nome} | Média: {sum(aluno.notas) / 4}")
            elif op == 6:
                for aluno in alunos:
                    file.write(f"{aluno.nome},{aluno.notas[0]},{aluno.notas[1]},{aluno.notas[2]},{aluno.notas[3]}\n")
                print("Os dados foram salvos!")
            elif op == 7:
                break
            else:
                print("Operação inválida!")


if __name__ == "__main__":
    main()
