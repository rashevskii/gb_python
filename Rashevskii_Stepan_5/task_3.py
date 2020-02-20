with open('task_3.txt', 'r', encoding='utf-8') as f_obj:
    salaries = []
    for_sum = []
    min_stuff = []
    lines = f_obj.readlines()
    for i in range(len(lines)):
        el_lines = lines[i].split()
        salaries.append(el_lines[1])
        for_sum.append(int(salaries[i]))
    sum_salaries = sum(for_sum)
    min_salaries = min(salaries)
    for i in range(len(lines)):
        stuff = lines[i].split()
        if min_salaries == stuff[1]:
            min_stuff.append(stuff[0])
    print(f'Сотрудник с наименьшим окладом: {" ".join(min_stuff)}')
    print(f'Средняя величина доходов сотрудников равна: {sum_salaries}')