def get_reverse_num(num):
    result = ''
    while num != 0:
        result += str(num % 10)
        num //= 10

    return int(result)


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
reversed_number_1 = get_reverse_num(number_1)
reversed_number_2 = get_reverse_num(number_2)

print(f'Первое число наоборот: {reversed_number_1}')
print(f'Второе число наоборот: {reversed_number_2}')
