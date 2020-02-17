import functools

numbers = [el for el in range(100, 1001) if el % 2 == 0]

print(functools.reduce(lambda a, b: a * b, numbers))

