text = input('Введите текст: ')
word_length = 0
max_word_length = 0

for letter in text + ' ':
    if letter != ' ':
        word_length += 1
    else:
        if word_length > max_word_length:
            max_word_length = word_length
        word_length = 0

print(f'Самое длинное слово, {max_word_length} букв')