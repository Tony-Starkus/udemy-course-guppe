vetor = [0, 1, 0, 2, 0, 3, 4, 5, 6, 0, 8, 8, 1, 0, 2]

for num in vetor:
    if num == 0:
        vetor.remove(num)

print(vetor)
exit()
print(list(filter(lambda x: x != 0, vetor)))
