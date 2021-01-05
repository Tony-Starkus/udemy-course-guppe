from random import randrange
a = randrange(100)
b = randrange(100)
pontos = 0
# 1
print(f"Quando é {a} + {b} ?")
r = int(input("Resposta: "))
if r == a + b:
    print("Certo!")
    pontos = pontos + 1
else:
    print(f"Errado! O resposta é: {a + b}")

# 2
a = randrange(100)
b = randrange(100)
print(f"Quando é {a} + {b} ?")
r = int(input("Resposta: "))
if r == a + b:
    print("Certo!")
    pontos = pontos + 1
else:
    print(f"Errado! O resposta é: {a + b}")

# 3
a = randrange(100)
b = randrange(100)
print(f"Quando é {a} + {b} ?")
r = int(input("Resposta: "))
if r == a + b:
    print("Certo!")
    pontos = pontos + 1
else:
    print(f"Errado! O resposta é: {a + b}")

# 4
a = randrange(100)
b = randrange(100)
print(f"Quando é {a} + {b} ?")
r = int(input("Resposta: "))
if r == a + b:
    print("Certo!")
    pontos = pontos + 1
else:
    print(f"Errado! O resposta é: {a + b}")

# 5
a = randrange(100)
b = randrange(100)
print(f"Quando é {a} + {b} ?")
r = int(input("Resposta: "))
if r == a + b:
    print("Certo!")
    pontos = pontos + 1
else:
    print(f"Errado! O resposta é: {a + b}")

print(f"Você acertou {pontos} questões")
