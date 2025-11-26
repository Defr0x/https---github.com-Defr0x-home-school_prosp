import numpy as np

nums = np.array([12, 45, 2, 78, 31, 5, 96, 14, 67, 23])

print(nums[nums > 30])
print(nums % 2 == 0)
nums[nums < 10] = -1
print(nums)