seq_count = int(input('Введите кол-во чисел: '))
prime_numbers = 0

for num_id in range(seq_count):
    number = int(input(f'Число {num_id + 1}: '))
    for divider in range(2, number):
        if number % divider == 0:
            break
    else:
        prime_numbers += 1

print(f'Простых чисел в последовательности: {prime_numbers}')