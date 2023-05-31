import numpy as np

d2_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# list style
print(d2_array[2][0], d2_array[-1][-3], d2_array[2][-3])
# numpy style
print(d2_array[2, 0], d2_array[-1, 0])

d2_array[0, 0] = 11
print(d2_array)

d2_array[0, 0] = 22.71
print(d2_array)