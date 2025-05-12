def get_max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def get_max_of_three(num1, num2, num3):
    num4 = get_max_of_two(num1, num2)
    if num4 > num3:
        return num4
    else:
        return num3


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

max_number = get_max_of_three(number_1, number_2, number_3)

print(f'Самое большое число: {max_number}')

