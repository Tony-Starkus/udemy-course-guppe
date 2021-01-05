num = int(input("Informe o número: "))
if num <= 1:
    print("O número precisa ser maior que 1!")
    exit()

for i in range(num, 0, -1):
    if i != 1 and i != num:
        if num % i == 0:
            print("Não é primo!")
            exit()
print("É primo!")
