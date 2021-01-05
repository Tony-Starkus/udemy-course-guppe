num = int(input("Digite um número inteiro: "))

a = 0
b = 0
c = 0

for i in range(num + 1):
    a = a + i

operacao = True
for j in range(1, 2 * num):
    if operacao:
        b = b + j
        operacao = False
    else:
        b = b - j
        operacao = True

for k in range(1, 2 * num, 2):
    c = c + k

print(a)
print(b)
print(c)
