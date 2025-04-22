x_pos = 8
y_pos = 10

while True:
    user_command = input(f'[Программа]: Марсоход находится на позиции {x_pos}, {y_pos}'
                         f' введите команду:\n[Оператор]: ')

    if user_command == 'W' and y_pos != 20:
        y_pos += 1
    elif user_command == 'S' and y_pos != 0:
        y_pos -= 1
    elif user_command == 'D' and x_pos != 15:
        x_pos += 1
    elif user_command == 'A' and x_pos != 0:
        x_pos -= 1

