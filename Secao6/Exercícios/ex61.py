valores = []
for i in range(100, 1000):
    for j in range(100, 1000):
        x = str(i * j)
        x_reversed = x[::-1]
        if x == x_reversed:
            print(x)
            valores.append(int(x))

print(f"Maior: {max(valores)}")
