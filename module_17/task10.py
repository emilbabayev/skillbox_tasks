# Юлий Цезарь использовал свой способ шифрования текста.
# Каждая буква заменялась на следующую по алфавиту через K позиций по кругу.
# Если взять русский алфавит и k = 3, то в слове,
# которое мы хотим зашифровать, буква А станет буквой Г, Б станет Д и так далее.
#
# Пользователь вводит сообщение, а также значение сдвига.
# Напишите программу, которая зашифрует это сообщение при помощи шифра Цезаря.

russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

message = input('Введите сообщение: ')
shift = int(input('Сдвиг - '))

message_symbols = [sym for sym in message]
caesar_cypher_symbols = [' ' if sym == ' '
                         else russian_alphabet[(russian_alphabet.index(sym) + shift) % 33]
                         for sym in message_symbols]

caesar_cypher = ''
for sym in caesar_cypher_symbols:
    caesar_cypher += sym

print('Зашифрованное сообщение:', caesar_cypher)