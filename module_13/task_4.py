def count_numbers(num):
    # Получает число и возвращает количество цифр в числе

    num_count = 0
    while num != 0:
        num_count += 1
        num //= 10

    return num_count


def change_number(num1):
    # Получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число

    digit_count = count_numbers(num1)

    last_digit = num1 % 10
    first_digit = num1 // 10 ** (digit_count - 1)
    between_digits = num1 % 10 ** (digit_count - 1) // 10

    result = last_digit * 10 ** (digit_count - 1) + between_digits * 10 + first_digit
    return result


def main():
    first_n = int(input("Введите первое число: "))
    second_n = int(input("Введите второе число: "))

    first_num_count = count_numbers(first_n)
    second_num_count = count_numbers(second_n)

    if first_num_count < 3:
        print("В первом числе меньше трёх цифр.")

    elif second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")

    else:
        first_n = change_number(first_n)
        second_n = change_number(second_n)

        print('Изменённое первое число:', first_n)
        print('Изменённое второе число:', second_n)
        print('\nСумма чисел:', first_n + second_n)


main()