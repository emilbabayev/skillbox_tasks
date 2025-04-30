first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

num_sum = first_num + second_num
num_diff = abs(first_num - second_num)

max_num = (num_sum + num_diff) // 2
print(f'Максимальное число: {max_num}')