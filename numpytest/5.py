import numpy as np

a = np.arange(25).reshape(5, 5)
print(a)
print()
print(a[:, 1])
print(a[-2:])
print(a[:2, -2:])
print(a[-1, -1])