import itertools


def factorial_gen():
    for el in itertools.count(1):
        num = 1
        if el > 25:
            break
        for i in range(1, el):
            num *= i + 1
        yield {el: num}


for el in factorial_gen():
    if list(el.keys())[0] > 15:
        break
    print(el)
