# На вход в программу подаётся строка, в которой буква h встречается как минимум два раза.
# Реализуйте код, который разворачивает последовательность символов,
# заключённую между первым и последним появлением буквы h, в противоположном порядке.

my_text = input('Текст: ')
symbols = [symbol for symbol in my_text]

h_index = [i for i in range(len(symbols)) if symbols[i] == 'h']

first_h_index = h_index[0]
last_h_index = h_index[-1]

symbols = symbols[first_h_index + 1:last_h_index]
symbols = symbols[::-1]

result = ''
for sym in symbols:
    result += sym

print('Результат:', result)