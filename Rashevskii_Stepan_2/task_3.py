# month_user = int(input('Введите номер месяца: '))

month_user = 5

list_of_months = [
    [12, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
]

winter = list_of_months[0]
spring = list_of_months[1]
summer = list_of_months[2]
autumn = list_of_months[3]

if month_user == winter[0] or month_user == winter[1] or month_user == winter[2]:
    print('У нас зима!')
elif month_user == spring[0] or month_user == spring[1] or month_user == spring[2]:
    print('У нас весна!')
elif month_user == summer[0] or month_user == summer[1] or month_user == summer[2]:
    print('У нас лето!')
else:
    print('У нас осень!')

dict_of_months = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11],
}

if month_user == dict_of_months['winter'][0] or month_user == dict_of_months['winter'][1] or month_user == \
        dict_of_months['winter'][2]:
    print('У нас зима!')
elif month_user == dict_of_months['spring'][0] or month_user == dict_of_months['spring'][1] or month_user == \
        dict_of_months['spring'][2]:
    print('У нас весна!')
elif month_user == dict_of_months['summer'][0] or month_user == dict_of_months['summer'][1] or month_user == \
        dict_of_months['summer'][2]:
    print('У нас лето!')
else:
    print('У нас осень!')
