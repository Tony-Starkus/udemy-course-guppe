n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a teceira nora: "))
media = (n1 + n2 + (n3 * 2)) / 3

if media >= 60:
    print(f"O aluno foi aprovado. Média: {round(media, 1)}")
else:
    print(f"O aluno não foi aprovado. Média: {round(media, 1)}")
