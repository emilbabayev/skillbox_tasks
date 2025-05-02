def count_letters(text):
    digit_to_found = input('Какую цифру ищем: ')
    letter_to_found = input('Какую букву ищем: ')

    digit_count = 0
    letter_count = 0

    for sym in text:
        if sym == digit_to_found:
            digit_count += 1
        elif sym == letter_to_found:
            letter_count += 1

    print(f'\nКоличество цифр {digit_to_found}: {digit_count}')
    print(f'Количество букв {letter_to_found}: {letter_count}')


user_text = input('Введите текст: ')
count_letters(user_text)