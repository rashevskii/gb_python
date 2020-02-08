# counter = 0
# list_len = 6
# my_list = []
# while counter < list_len:
#    my_list.append((input('Enter: ')))
#    counter += 1

my_list = [1, 2, 3, 4, 5, 6]
index = 0
counter = 0
if len(my_list) % 2 == 0:
    while counter < len(my_list):
        my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
        index += 2
        counter += 2
elif len(my_list) % 2 != 0:
    while counter < len(my_list) - 1:
        my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
        index += 2
        counter += 2

print(my_list)
