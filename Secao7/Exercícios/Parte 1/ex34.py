vetor = []

while len(vetor) < 10:
    num = float(input("Informe um número: "))
    if num.is_integer():
        num = int(num)
    if num in vetor:
        print("Este número já existe no vetor")
    else:
        vetor.append(num)

print(vetor)
