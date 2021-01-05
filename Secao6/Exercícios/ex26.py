from sys import maxsize

num = int(input("Digite um número inteiro: "))

for i in range(num + 1, maxsize**10):
    if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
        print(i)
        break
