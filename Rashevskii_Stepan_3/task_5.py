def sum_numbers():
    sum_of_numbers = 0
    count = 1
    end = 0
    while True:
        user_numbers = (input('Введите любой набор чисел через пробел. Для выхода нажмите q и enter: '))
        as_list = user_numbers.split()
        numbers = []
        without_q_list = list(filter(lambda x: x != 'q', as_list))
        for elem in without_q_list:
            numbers.append(int(elem))
        sum_of_numbers += sum(numbers)
        print(sum_of_numbers)
        for elem in as_list:
            if elem == 'q':
                end = 1
        count += 1
        if end == 1:
            break


sum_numbers()
