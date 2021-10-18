import math

print('Введите координаты монетки: ')
x = float(input('Х: '))
y = float(input('Y: '))

if math.sqrt(x ** 2 + y ** 2) > 1:
    print('Монетки нет поблизости')
else:
    print('Монетка где-то рядом!')

