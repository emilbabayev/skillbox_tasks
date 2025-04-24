pyramid_height = int(input('Введите высоту пирамиды: '))
start_number = 1

for spaces in range(pyramid_height, - 1, -1):
    print('\t' * spaces, end='')
    for number in range(pyramid_height - spaces + 1):
        print(str(start_number) + '\t', end='\t')
        start_number += 2
    print()