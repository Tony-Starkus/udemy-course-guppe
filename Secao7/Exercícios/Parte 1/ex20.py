vetor1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
vetor2 = []

for i in vetor1:
    if i % 2 == 1:
        vetor2.append(i)

for i in range(0, 10, 2):
    print(f"{vetor1[i]} | {vetor1[i + 1]}")

for i in range(0, len(vetor2), 2):
    if i == len(vetor2) - 1:
        print(f"{vetor2[i]}")
        continue
    print(f"{vetor2[i]} | {vetor2[i + 1]}")
