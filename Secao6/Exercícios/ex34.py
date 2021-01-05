from sys import maxsize
menor = 0
x = True

for i in range(1, maxsize):
    x = True
    for j in range(1, 21):
        print(f"{i} % {j} = {i % j}")
        if i % j != 0:
            x = False
    if x:
        print(i)
        break
