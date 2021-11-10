# Дана строка, содержащая пробелы.
# Найдите в ней самое длинное слово, выведите  это слово и его длину.
# Если таких слов несколько, выведите первое из них.

message = input('Введите строку: ').split()

words_length = [len(word) for word in message]
max_length = max(words_length)
longest_word = message[words_length.index(max_length)]

print('Максимальная длина слова: {}'.format(max_length))
print('Самое длинное слово: {}'.format(longest_word))