rows = int(input('Введите кол-во рядов: '))
seats = int(input('Введите кол-во сидений: '))
distance_between_rows = int(input('Введите кол-во метров между рядами: '))

print('Сцена\n')

for row in range(rows):
    print('=' * seats, end=' ')
    print('*' * distance_between_rows, end=' ')
    print('=' * seats)