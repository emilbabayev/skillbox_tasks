# Пользователь вводит строку.
# Напишите программу, которая изменяет регистр символов в этой строке так,
# чтобы первая буква каждого слова была заглавной, а остальные буквы — строчными.

message_words = input('Введите строку: ').split()

for i_word in range(len(message_words)):
    message_words[i_word] = message_words[i_word].title()

print('Результат: {}'.format(' '.join(message_words)))