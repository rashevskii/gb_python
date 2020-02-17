import itertools
test_list = [1, 2, 3, 4]

for el in itertools.count(56):
    if el > 100:
        break
    print(el)

count = 0
for el in itertools.cycle(test_list):
    if count > 20:
        break
    print(el)
    count += 1
