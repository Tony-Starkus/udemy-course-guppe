valores = []

for i in range(2000000, 0, -1):
    primo = True
    for j in range(i - 1, 1, -1):
        if i % j == 0:
            primo = False
            break

    if primo:
        valores.append(i)
        print(f"{i} é primo!")
    else:
        print(i)

print(f"Somatório: {sum(valores)}")
print(f"Tamanho da lista: {len(valores)}")
