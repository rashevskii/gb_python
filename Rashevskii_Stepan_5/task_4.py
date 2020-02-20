my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('task_4.txt', 'r', encoding='utf-8') as f_obj:
    text_file = f_obj.readlines()

list_lines = []
for i in range(len(text_file)):
    list_lines.append(text_file[i].split())

with open('task_4_2.txt', 'w', encoding='UTF-8') as new_f_obj:
    for i in range(len(list_lines)):
        key = list_lines[i][0]
        if key in my_dict:
            new_f_obj.write(f'{my_dict[key]} - {i+1}\n')
