# proceeds = int(input('Введите выручку вашей фирмы: '))
# costs = int(input('Введите издержки вашей фирмы: '))

proceeds = 1000
costs = 500

if proceeds > costs:
    print('Ваша фирма приносит вам прибыль')
    print(f'Соотношение прибыли к выручке - {proceeds // costs}')
    # number_stuff = int(input('Введите количество сортудников вашей фирмы: '))
    number_stuff = 10
    print(f'Прибыль на каждого сотрудника состовляет: {proceeds // number_stuff}')
elif proceeds < costs:
    print('Вы работаете в убыток')
else:
    print('Вы работаете в 0')
