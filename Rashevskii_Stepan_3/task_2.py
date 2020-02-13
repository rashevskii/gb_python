def human(first_name, last_name, year, city, email, phone):
    return f'First_name: {first_name}, last_name: {last_name}, year of born: {year}, city: {city}, email: {email}, ' \
           f'phone: {phone}'


my_kwargs = {
    'first_name': 'Ivan',
    'last_name': 'Ivanov',
    'year': 1980,
    'city': 'Moscow',
    'email': 'ivanov@mail.ru',
    'phone': 919746311,
}


print(human(first_name='Ivan', last_name='Ivanov', year=1980, city='Moscow', email='ivanov@mail.ru', phone=919746311))
print(human(**my_kwargs))

