"""
1h = 3600s
"""
entrada = int(input("Valor em segundos: "))
horas = 0
minutos = 0

while entrada >= 3600:
    horas = horas + 1
    entrada = entrada - 3600

while entrada >= 60:
    minutos = minutos + 1
    entrada = entrada - 60

print(f"{horas}:{minutos}:{entrada}")
