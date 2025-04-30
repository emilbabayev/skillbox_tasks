result = False

print('Введите местоположение коня:')
x_cord = float(input())
y_cord = float(input())


if x_cord < 0 or x_cord > 0.8 or y_cord < 0 or y_cord > 0.8:
    print('Ошибка ввода местоположения')
else:
    x_cord = int(x_cord * 10)
    y_cord = int(y_cord * 10)

    print('Введите местоположение точки на доске:')
    destination_x_cord = float(input())
    destination_y_cord = float(input())

    destination_x_cord = int(destination_x_cord * 10)
    destination_y_cord = int(destination_y_cord * 10)

    diff_x = abs(destination_x_cord - x_cord)
    diff_y = abs(destination_y_cord - y_cord)

    if diff_x == 2 or diff_y == 2:
        if diff_x == 1 or diff_y == 1:
            result = True

    print(f'Конь в клетке ({x_cord}, {y_cord}). Точка в клетке ({destination_x_cord},{destination_y_cord})')

    if result:
        print('Да, конь может ходить в эту точку.')
    else:
        print('Нет, конь не может ходить в эту точку')