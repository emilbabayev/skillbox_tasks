def get_gcd(num_a, num_b):
    while num_a != 0 and num_b != 0:
        if num_a > num_b:
            num_a %= num_b
        else:
            num_b %= num_a

    print(f'НОД = {num_a + num_b}')


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

get_gcd(num_1, num_2)