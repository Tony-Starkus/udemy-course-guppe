import sys
sys.tracebacklimit = 0

a = float(input("Informe um número positivo menor que 1000: "))
if a >= 1000:
    raise Exception('Valor não é menor que 1000')
if a.is_integer():
    a = int(a)
b = float(input("Informe um número positivo menor que 1000: "))
if b >= 1000:
    raise Exception('Valor não é menor que 1000')
if b.is_integer():
    b = int(b)

vetor1 = [int(x) for x in str(a)]
vetor1.sort()
vetor2 = [int(x) for x in str(b)]
vetor2.sort()
print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor 1 + Vetor 2 = {list(sum(x) for x in zip(vetor1, vetor2))}")
