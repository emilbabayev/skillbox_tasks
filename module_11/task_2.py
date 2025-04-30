import math

seq_count = int(input('Введите кол-во чисел: '))

for num_id in range(seq_count):
    number = float(input('Введите число: '))

    if number > 0:
        number = math.ceil(number)
        result = math.log(number)
        print(f'x = {number}, log(x) = {result}')
    else:
        number = math.floor(number)
        result = math.exp(number)
        print(f'x = {number}, exp(x) = {result}')