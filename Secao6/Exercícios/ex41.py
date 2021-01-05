
while True:
    R1 = float(input("Informe o R1: "))
    if R1 == 0:
        break
    if R1.is_integer():
        R1 = int(R1)

    R2 = float(input("Informe o R2:"))
    if R2 == 0:
        break
    if R2.is_integer():
        R2 = int(R2)

    R = (R1 * R2) / (R1 + R2)
    print(R)
