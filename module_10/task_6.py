pyramid_height = int(input('Введите высоту пирамиды: '))

for lvl in range(pyramid_height):
    print(' ' * (pyramid_height - lvl - 1), end='')
    print('#' * (lvl * 2 + 1), end='')
    print(' ' * (pyramid_height - lvl - 1))
