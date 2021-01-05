num = int(input("Digite um número entre 100 e 999: "))

if num not in range(100, 1000):
    print("O número não está entre 100 e 999")
else:
    x = str(num)
    for i in x:
        print(i)
