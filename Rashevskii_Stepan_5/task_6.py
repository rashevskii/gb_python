with open('task_6.txt', 'r', encoding='UTF-8') as f_obj:
    lines = f_obj.readlines()
    print(lines)

list_num = []
for i in range(len(lines)):
    list_num.append(lines[i].split(' '))
# print(list_num)

list_num_2 = []
list_num_3 = []
for i in range(len(list_num)):
    for j in range(len(list_num[i])):
        list_num_2.append(list_num[i][j].split())
# print(list_num_2)
for i in range(len(lines)):
    list_num_3 = lines[i].strip('(лпрлаб)')
    # list_num_3.append(list_num_2[i].strip('(лпрлаб)'))
    # list_num_3 = list_num_2[i].strip()
    print(list_num_3)

