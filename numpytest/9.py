import numpy as np

linear = np.arange(1, 13)
a = linear.reshape(3, 4)
print(a)
print(linear.reshape(2, 3, 2))
print(a.flatten())