valores = []
for i in range(1, 1000):
    if i % 3 == 0 and i% 5 == 0:
        valores.append(i)

print(sum(valores))
