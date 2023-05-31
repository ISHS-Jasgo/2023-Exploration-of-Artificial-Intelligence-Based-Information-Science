import numpy as np

d2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(d2)

print(d2[::2][::2])
print(d2[::2, ::2])

print(d2[0:2, 2:])
print(d2[0])
print(d2[1], d2[1, :])
print(d2[:, 2:3])
print(d2[:, 2])
print(d2[0:2, 0:2])
print(d2[1::2, 1::2])
