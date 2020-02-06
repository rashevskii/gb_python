# time = int(input('Введите время в секундах: '))

time = 2500

hours = time // 3600
minutes = (time // 60) % 60
seconds = time % 60

if hours < 10:
    hours = '0' + str(hours)
else:
    hours = hours

if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = minutes

if seconds < 10:
    seconds = '0' + str(seconds)
else:
    seconds = seconds

print(f'{hours}:{minutes}:{seconds}')
