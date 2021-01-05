import numpy as np
from random import random
# A = np.array([int(random() * 100) for _ in range(9)]).reshape(3, 3)
A = np.arange(0, 9).reshape(3, 3)
B = np.arange(10, 19).reshape(3, 3)

print(np.matmul(A, B))
