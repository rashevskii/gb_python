with open('task_2.txt', 'r') as f_obj:
    lines = f_obj.readlines()
    print(f'Количество строк в файле {len(lines)}')
    for i in range(len(lines)):
        print(f'Количество слов в {i+1} строке {len(lines[i].split())}')
