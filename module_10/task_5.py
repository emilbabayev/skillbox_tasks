seq_count = int(input('Введите кол-во чисел: '))
max_digit_sum = 0
max_digit_number = 0

for num_id in range(seq_count):
    number = int(input(f'Число {num_id + 1}: '))
    digit_sum = 0
    number_copy = number

    while number_copy != 0:
        digit_sum += number_copy % 10
        number_copy //= 10

    if digit_sum > max_digit_sum:
        max_digit_sum = digit_sum
        max_digit_number = number

print(f'Число {max_digit_number} имеет максимальную сумму цифр: {max_digit_sum}')