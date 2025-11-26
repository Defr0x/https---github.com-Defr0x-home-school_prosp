import numpy as np

scores = np.array([75, 42, 98, 55, 67, 89, 91, 78, 63, 84, 51, 72, 95, 81, 36, 47, 100, 69, 88, 57])

print(np.mean(scores))
print(np.max(scores))
print(np.min(scores))
print(np.sum(scores >= 85))
print(np.sum(scores < 60))


print(np.minimum(scores + 5, 100))