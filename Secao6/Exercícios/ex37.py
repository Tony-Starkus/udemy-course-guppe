valores = []
for i in range(1000, 10000):
    x = int(str(i)[:2])
    y = int(str(i)[-2:])
    r1 = x + y
    if r1**2 == i:
        valores.append(i)

print(valores)
