var_1 = int(input('Введите число: '))
var_2 = int(input('Введите второе число: '))


def division(v_1, v_2):
    if v_2 != 0:
        return v_1 / v_2
    else:
        return 'На ноль делить нельзя!'


print(division(var_1, var_2))
