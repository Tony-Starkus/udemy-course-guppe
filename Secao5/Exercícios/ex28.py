op = input("Informe a operação:\n"
           "(a) Geométrica\n"
           "(b) Ponderada\n"
           "(c) Harmônica\n"
           "(d) Aritmética\n"
           "Opção: ")

if op not in ('a', 'b', 'c', 'd'):
    print("Operação inválida!")
    exit()

print("Informe os valores:")
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

if op == 'a':
    r = (x * y * z) ** (1/3)
    print(f"Resultado: {r}")
elif op == 'b':
    r = ((x + 2) * (y + 3) * z) / 6
    print(f"Resultado: {r}")
elif op == 'c':
    r = 1 / ((1 / x) + (1 / y) + (1 / z))
    print(f"Resultado: {r}")
elif op == 'd':
    r = (x + y + z) / 3
    print(f"Resultado: {r}")
