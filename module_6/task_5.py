guess_number = 7
guesses = 0

while True:
    player_number = int(input('Введите число: '))
    if player_number == guess_number:
        print(f'Вы угадали. Число попыток {guesses}')
        break
    elif player_number > guess_number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    guesses += 1