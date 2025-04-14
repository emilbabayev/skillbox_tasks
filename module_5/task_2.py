x = int(input('Введите число x: '))

if x > 0:
    y = x - 12
elif x == 0:
    y = 5
else:
    y = x ** 2

print(f'y = {y}')