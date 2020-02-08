# user_string = input('Введите произвольную строку: ')
user_string = 'I love pythonpythonpython'
format_string = user_string.split()

for elem, item in enumerate(format_string):
    print(elem + 1, item[:10])

for i in range(len(format_string)):
    print(i + 1, format_string[i][:10])
