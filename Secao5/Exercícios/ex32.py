cardapio = {
            100: 1.20,
            101: 1.30,
            102: 1.50,
            103: 1.20,
            104: 1.70,
            105: 2.20,
            106: 1
            }

cod = int(input("Digite o código do produto: "))
qtd = int(input("Digite a quatidade: "))
print(f"O valor a ser pago: {cardapio[cod] * qtd}")
