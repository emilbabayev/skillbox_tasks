def get_digit_count(num):
    digits = 0

    if num >= 1:
        while num != 0:
            digits += 1  # кол-во цифр в числе
            num //= 10

    else:
        while num < 1:
            digits += 1  # кол-во нулей в числе
            num *= 10

    return digits


number = float(input('Введите число: '))

if number < 0:
    print('Ошибка. Введено отрицательное число')

elif number >= 1:
    mantissa = number / (10 ** (get_digit_count(number) - 1))
    order = get_digit_count(number) - 1
    print(f'Формат плавающей точки: x = {mantissa} * 10 ** {order}')

else:
    mantissa = number * (10 ** get_digit_count(number))
    order = -1 * get_digit_count(number)
    print(f'Формат плавающей точки: x = {mantissa} * 10 ** {order}')

