import math

graus = float(input("Digite o ângulo em graus: "))
radiano = (graus * math.pi) / 180
print(f"O valor em radianos é: {round(radiano, 4)}")
