def upper_letter(user_enter):
    # user_enter = input('Enter a string with spaces: ')
    res_string = ' '
    list_of_words = user_enter.split()
    list_of_words_2 = []
    for elem in list_of_words:
        list_of_words_2.append(f'{elem[:1].upper()}{elem[1:]}')
    result = res_string.join(list_of_words_2)
    return result


print(upper_letter('one two three'))
