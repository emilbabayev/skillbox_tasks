# Числа Фибоначчи — это ряд чисел, в котором каждое следующее число равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …
#
# Пользователь вводит num_pos.
# Напишите функцию, которая выводит число, которое стоит на позиции num_pos в ряде Фибоначчи.

def fibonacci(stop_num):
    if stop_num <= 1:
        return stop_num
    else:
        return fibonacci(stop_num - 1) + fibonacci(stop_num - 2)


num_pos = int(input('Введите число: '))
print('Число на позиции {} в ряде Фибоначчи: {}'.format(num_pos, fibonacci(num_pos)))
