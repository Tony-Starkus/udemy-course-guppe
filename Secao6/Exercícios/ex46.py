from random import randrange
x = randrange(1, 1001)
acertou = False
tentativas = 0

while not acertou:
    num = int(input("Digite um número: "))
    if num == x:
        print("Acertou!")
        print(f"Tentativas: {tentativas}")
        acertou = True
    elif num > x:
        print("Menos!")
        tentativas = tentativas + 1
    elif num < x:
        print("Mais!")
        tentativas = tentativas + 1
