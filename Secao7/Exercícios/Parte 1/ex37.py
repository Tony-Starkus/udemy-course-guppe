vetor = [1.1, 2.2, 3.3, 10.8, 9.5, 30.2, 293.12, 203.12, 450.34, 9304.3, 20.1]
maior = max(vetor)
vetor.remove(maior)
vetor.sort()
vetor_esquerda = vetor[0:5]
vetor_direita = vetor[-5:]
vetor_direita.sort(reverse=True)
print(vetor_esquerda + [maior] + vetor_direita)