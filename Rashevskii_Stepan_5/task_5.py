import random

with open('task_5.txt', 'w', encoding='UTF-8') as f_obj:
    numbers = []
    for i in range(20):
        numbers.append(str(random.randrange(100)))
        f_obj.writelines(f'{numbers[i]} ')

with open('task_5.txt', 'r', encoding='UTF-8') as f_obj:
    numbers = f_obj.read().split()

nums = map(lambda x: int(x), numbers)
print(f'Сумма всех чисел: {sum(nums)}')
