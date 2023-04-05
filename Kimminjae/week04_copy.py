import copy

a = [-9, [77, 13], 100]
b = a[:]  # copy
c = list(a)  # copy
d = a.copy()  # copy
e = copy.deepcopy(a)  # deep copy
print(id(a), id(b), id(c), id(d), id(e))
b[1][0] = 16
print(a, b, c, d, e)
