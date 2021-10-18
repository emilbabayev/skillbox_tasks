def digit_count(number):
    result = 0
    while number != 0:
        number //= 10
        result += 1
    return result


def digit_sum(number):
    result = 0
    while number != 0:
        result += number % 10
        number //= 10
    return result


x = int(input('Введите число: '))
print('Сумма цифр:', digit_sum(x))
print('Кол-во цифр в числе:', digit_count(x))
print('Разность суммы и кол-ва цифр:', digit_sum(x) - digit_count(x))