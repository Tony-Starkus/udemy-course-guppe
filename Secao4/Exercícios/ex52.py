j1 = float(input("Digite o investimento do jogador 1: "))
j2 = float(input("Digite o investimento do jogador 2: "))
j3 = float(input("Digite o investimento do jogador 3: "))
premio = float(input("Digite o valor do prêmio: "))
total_inv = j1 + j2 + j3
p1 = float((j1 * 100) / total_inv)
p2 = float((j2 * 100) / total_inv)
p3 = float((j3 * 100) / total_inv)

print(f"O jogador 1 vai receber: {(premio * p1) / 100}")
print(f"O jogador 2 vai receber: {(premio * p2) / 100}")
print(f"O jogador 3 vai receber: {(premio * p3) / 100}")
