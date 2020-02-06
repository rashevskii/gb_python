# number = int(input('Введите любое положительное число: '))

number = 564051

result = 0

while number > 0:
    digit = number % 10
    number = number // 10
    if digit > result:
        result = digit

print(result)

