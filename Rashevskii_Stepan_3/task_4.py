def my_func(x, y):
    y *= -1
    count = 1
    x_var = x
    while count < y:
        x_var *= x
        count += 1
    return 1 / x_var


print(my_func(5, -5))
