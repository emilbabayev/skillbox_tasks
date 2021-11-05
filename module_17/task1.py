# Команде лингвистов понравилось качество ваших программ, и они решили заказать у вас функцию для анализатора текста,
# которая создавала бы список гласных букв текста, а заодно считала бы их количество.
#
# Напишите программу, которая запрашивает у пользователя текст и генерирует список из гласных букв этого
# текста (сама строка вводится на русском языке). Выведите в консоль сам список и его длину.

user_text = input('Ваш текст: ')

# Гласные - а, у, о, ы, и, э, я, ю, ё, е
vowel_letters = [letter for letter in user_text
                 if letter == 'а' or letter == 'А' or
                 letter == 'у' or letter == 'У' or
                 letter == 'о' or letter == 'О' or
                 letter == 'ы' or letter == 'Ы' or
                 letter == 'и' or letter == 'И' or
                 letter == 'э' or letter == 'Э' or
                 letter == 'я' or letter == 'Я' or
                 letter == 'ю' or letter == 'Ю' or
                 letter == 'ё' or letter == 'Ё' or
                 letter == 'е' or letter == 'Е']

print('Гласные буквы текста:', vowel_letters)