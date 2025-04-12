kostya_roll = int(input('Кубик Кости: '))
owner_roll = int(input('Кубик владельца: '))

summ = kostya_roll + owner_roll

if kostya_roll >= owner_roll:
    print('\nИгрок платит!')
else:
    print(f'\nСумма: {summ}')
    print('Владелец платит')

print('Игра окончена')