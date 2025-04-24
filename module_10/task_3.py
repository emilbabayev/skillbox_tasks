width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))

for row in range(height):
    for col in range(width):
        if col == 0 or col == width - 1:
            print('|', end='')
        elif row == 0 or row == height - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print()