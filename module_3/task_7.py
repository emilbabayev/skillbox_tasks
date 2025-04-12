number = int(input('Введите 4х-значное число: '))

digit_1 = number // 1000
digit_2 = number // 100 % 10
digit_3 = number // 10 % 10
digit_4 = number % 10

print(f'Цифры числа {number}: {digit_1} {digit_2} {digit_3} {digit_4}')

