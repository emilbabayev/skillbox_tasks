def reverse_number(number):
    new_num = ''
    number = str(number)
    integer_part = int(number.split('.')[0])
    fractional_part = int(number.split('.')[1])

    while integer_part != 0:
        new_num += str(integer_part % 10)
        integer_part //= 10

    new_num += '.'

    while fractional_part != 0:
        new_num += str(fractional_part % 10)
        fractional_part //= 10

    new_num = float(new_num)
    return new_num


print(reverse_number(123.321))
