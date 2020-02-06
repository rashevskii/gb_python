a = 4
b = 9
count_days = 1
print(f'1-й день: {a}')
while a <= b:
    count_days += 1
    a = round(a + ((a * 10) / 100), 2)
    print(f'{count_days}-й день: {a}')

print(f'На {count_days}-й день спортсмен достиг результата - не менее {b} км.')

