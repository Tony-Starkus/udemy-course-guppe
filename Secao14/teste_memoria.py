"""
Teste de Memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...
"""

# Função usando listas - 449mb de memória


def fib_lista(__max__):
    nums = []
    a, b = 0, 1
    while len(nums) < __max__:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib_lista(100):
    print(n)


# Função usando geradores - 3mb de memória

def fib_gen(__max__):
    a, b, contador = 0, 1, 0
    while contador < __max__:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste
for n in fib_gen(100):
    print(n)
