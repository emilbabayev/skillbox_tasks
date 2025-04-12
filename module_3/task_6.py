num_1 = int(input('Введите 1ое число: '))
num_2 = int(input('Введите 2ое число: '))

result = num_1 % 10 + num_2 % 10

print(f'Сумма последних цифр чисел {num_1} и {num_2}: {result}')