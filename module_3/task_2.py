quarter_1 = int(input('Доход по 1му кварталу: '))
quarter_2 = int(input('Доход по 2му кварталу: '))
quarter_3 = int(input('Доход по 3му кварталу: '))
quarter_4 = int(input('Доход по 4му кварталу: '))

first_half = quarter_1 + quarter_2
second_half = quarter_3 + quarter_4

result = first_half / second_half
print(f'Динамика: {result}')