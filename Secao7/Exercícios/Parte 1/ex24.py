alunos = {1: 2.0, 2: 5.0, 3: 1}

for i in range(10):
    x = input("Informe o ID do aluno e sua altura, separado por espaço: ").split()
    alunos.update({int(x[0]): float(x[1])})

maior = max(alunos, key=alunos.get)
menor = min(alunos, key=alunos.get)
print(f"Maior ID {maior}: {alunos[maior]}")
print(f"Menor ID {menor}: {alunos[menor]}")
