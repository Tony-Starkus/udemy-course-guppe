"""
Código do consumidor: {1: Residencial, 2: Comercial, 3: Industrial}
"""

total_hab = int(input("Informe o número de habitantes: "))
kwh = float(input("Informe o kwh: "))
if kwh.is_integer():
    kwh = int(kwh)

habitantes = {}
for i in range(1, total_hab + 1):
    cod = int(input("1- Residencial\n2- Comercial\n3- Industrial\nOpção: "))
    consumo = float(input("Consumo: "))
    if consumo.is_integer():
        consumo = int(consumo)
    habitantes.update({i: {"codigo": cod, "consumo": consumo}})

Tipo1 = 0
Tipo2 = 0
Tipo3 = 0
lista_consumo = []
for item, value in habitantes.items():
    lista_consumo.append(value['consumo'])
    if value['codigo'] == 1:
        Tipo1 = Tipo1 + value['consumo']
    elif value['codigo'] == 2:
        Tipo2 = Tipo2 + value['consumo']
    elif value['codigo'] == 3:
        Tipo3 = Tipo3 + value['consumo']

print(f"Residencial: {Tipo1}")
print(f"Comercial: {Tipo2}")
print(f"Industrial: {Tipo3}")
print(f"Maior consumo: {max(lista_consumo)}")
print(f"Menor consumo: {min(lista_consumo)}")
print(f"Média consumo: {sum(lista_consumo) / len(lista_consumo)}")
