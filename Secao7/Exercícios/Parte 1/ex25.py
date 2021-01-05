vetor = []

for i in range(1, 101):
    if i % 7 == 1:
        vetor.append(i)
    elif str(i)[-1] == "7":
        vetor.append(i)

print(vetor)
