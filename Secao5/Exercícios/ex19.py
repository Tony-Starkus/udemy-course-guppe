num = int(input("Digite um número: "))

x1 = num % 3
x2 = num % 5

if x1 == 0 and x2 == 0:
    print(f"O número é divisível por 3 e 5")
elif x1 == 0:
    print("O número é divisível por 3")
elif x2 == 0:
    print("O número é divisível por 5")
else:
    print("O número não é divisível por 3 e 5")
