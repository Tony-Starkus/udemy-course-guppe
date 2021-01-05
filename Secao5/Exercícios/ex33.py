preco = float(input("Digite o preço do produto: "))

x = 0
if preco >= 50:
    x = (preco * 5) / 100
elif 50.1 >= preco <= 100:
    x = (preco * 10) / 100
else:
    x = (preco * 15) / 100

if preco + x <= 80:
    print("Barato")
elif 80.1 >= preco <= 120:
    print("Normal")
elif 120.1 >= preco <= 200:
    print("Caro")
else:
    print("Muito caro")
