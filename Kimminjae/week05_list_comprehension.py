# def squares(number):
#     return number ** 2
#
#
# n = list(map(squares, range(1, 6)))
# print(n)
#
# n = list(map(lambda x: x ** 2, range(1, 6)))
# print(n)

# list comprehension (more pythonic)
n = [x ** 2 for x in range(1, 6)]
print(n)