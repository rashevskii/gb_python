my_list = [23, 3, 5, 67, 12, 3, 87]


def my_generator(some_list):
    for i in range(len(some_list)):
        if i == 0:
            continue
        elif some_list[i] > some_list[i - 1]:
            yield some_list[i]


my_new_list = list(my_generator(my_list))


print(my_new_list)
