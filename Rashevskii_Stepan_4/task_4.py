my_list = [12, 2, 12, 34, 76, 2, 45, 59]

some = [el for el in my_list if my_list.count(el) == 1]

print(some)
