nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite o número de faltas: "))

if 0 >= nota <= 3.9:
    print('E' if faltas > 20 else 'E')
elif 4 >= nota <= 4.9:
    print('D' if faltas > 20 else 'E')
elif 5 >= nota <= 7.4:
    print('C' if faltas > 20 else 'D')
elif 7.5 >= nota <= 8.9:
    print('B' if faltas > 20 else 'B')
else:
    print('B' if faltas > 20 else 'A')
