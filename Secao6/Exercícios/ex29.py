s = 0
for i in range(1, 6):
    s = s + (i / sum(list(range(i*2, 0, -1))))
print(s)
