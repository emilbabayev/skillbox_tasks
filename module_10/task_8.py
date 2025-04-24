pit_depth = int(input('Введите число: '))

for row in range(1, pit_depth + 1):
    for left_number in range(pit_depth, pit_depth - row, -1):
        print(left_number, end='')

    dots_count = (pit_depth - row) * 2
    print('.' * dots_count, end='')

    for right_number in range(pit_depth - row + 1, pit_depth + 1):
        print(right_number, end='')

    print()