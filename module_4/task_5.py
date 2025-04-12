number = int(input('Введите число: '))
new_number = number

if number < 0:
    new_number *= -1

print(f'|{number}| = {new_number}')