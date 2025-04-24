size = int(input('Введите число: '))

for row in range(1, size + 1):
    print((str(row) + ' ') * row, end='\t')
    for col in range(size):
        print(' ', end='\t')
    print()