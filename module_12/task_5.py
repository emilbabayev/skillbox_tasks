def rock_paper_scissors(vs_choice):
    """
    :param vs_choice: Выбор соперника. Камень - 1, Ножницы - 2, Бумага - 3
    :return: None
    """

    user_choice = int(input('Камень - 1, Ножницы - 2, Бумага - 3 '))
    win = False
    draw = False

    if user_choice > 3 or user_choice < 1:
        print('Ошибка ввода\n')
        rock_paper_scissors(vs_choice)

    if user_choice == 1 and vs_choice == 2:
        win = True
    elif user_choice == 1 and vs_choice == 3:
        win = False
    elif user_choice == 2 and vs_choice == 1:
        win = False
    elif user_choice == 2 and vs_choice == 3:
        win = True
    elif user_choice == 3 and vs_choice == 1:
        win = True
    elif user_choice == 3 and vs_choice == 2:
        win = False
    else:
        draw = True

    if win:
        print('Вы победили\n')
    elif not win and not draw:
        print('Вы проиграли\n')
    else:
        print('Ничья\n')

    main_menu()


def guess_the_number(secret_num):
    number = int(input('Угадай число: '))
    if number == secret_num:
        print('Ты угадал!\n')
    else:
        print('Не угадал\n')
        guess_the_number(secret_num)

    main_menu()


def main_menu():
    print('''Выберите игру
1 - Камень, ножницы, бумага
2 - Угадай число''')
    game_selection = int(input())

    if game_selection == 1:
        rock_paper_scissors(2)    # Камень - 1, Ножницы - 2, Бумага - 3
    elif game_selection == 2:
        guess_the_number(19)    # менять загаданное число тут


main_menu()