"""
Módulos Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.
"""

# Importar
from collections import deque

# Criando deques
deq = deque('geek')
print(deq)

# Adicionando elementos no deque
deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('k')  # Adiciona no começo
print(deq)

# Remover elementos

