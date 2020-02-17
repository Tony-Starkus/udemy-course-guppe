"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

# O all funciona como o operador lógico 'E', e o any funciona como 'OU'.

# Exemplo all()
print(all([0, 1, 2, 3, 4]))  # 0 (Zero) é false, então o retorno é False. Sem o zero, o retorno é True.
print(all([1, 2, 3, 4]))  # True
print(all([]))  # True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))  # Verdadeiro

# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

"""

print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, {}, (), []]))  # False
print(any([0, False, {}, (), [], 1]))  # True. Pois o '1' é verdadeiro. False 'OU' True == True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))  # True

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))  # True
