def my_func(num_1, num_2, num_3):
    list_of_numbers = [num_1, num_2, num_3]
    result_list = []
    result_list.append(max(list_of_numbers))
    list_of_numbers.remove(result_list[0])
    result_list.append(max(list_of_numbers))
    result = sum(result_list)
    return result


print(my_func(1, 2, 3))
