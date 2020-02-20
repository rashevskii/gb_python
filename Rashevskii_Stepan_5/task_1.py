enter = input('Enter text: ')
while enter != '':
    with open('text.txt', 'a') as f_obj:
        f_obj.write(f'{enter}\n')
    enter = input('Enter text: ')



