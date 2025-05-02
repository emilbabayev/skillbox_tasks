def main():
    print()
    user_number = int(input('Введите число: '))

    print('''Введите номер действия:
1 - сумма цифр
2 - максимальная цифра
3 - минимальная цифра:''')
    choice = int(input())

    if choice == 1:
        get_digit_sum(user_number)
    elif choice == 2:
        get_max_digit(user_number)
    elif choice == 3:
        get_min_digit(user_number)
    else:
        print('Ошибка ввода ')
        main()


def get_digit_sum(num):
    result = 0
    while num != 0:
        result += num % 10
        num //= 10

    print(f'Сумма цифр: {result}')
    main()


def get_max_digit(num):
    result = 0

    while num != 0:
        last_digit = num % 10
        if result == 9:
            break
        elif last_digit > result:
            result = last_digit

        num //= 10

    print(f'Максимальная цифра: {result}')
    main()


def get_min_digit(num):
    result = 9

    while num != 0:
        last_digit = num % 10
        if result == 0:
            break
        elif last_digit < result:
            result = last_digit

        num //= 10

    print(f'Минимальная цифра: {result}')
    main()


main()