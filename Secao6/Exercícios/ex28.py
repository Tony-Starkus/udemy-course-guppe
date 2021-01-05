N = int(input("Digite um valor inteiro e positivo: "))

if N < 0:
    print("O valor não é positivo")
else:
    E = 0
    for i in range(1, N + 1):
        E = E + (1 / sum(list(range(i, 0, -1))))
    print(E)
