# С увеличением объёма данных возникла потребность в сжатии этих данных,
# при этом без потери важной информации. Для этого было придумано кодирование, которое осуществляется следующим образом:
#
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
# то есть группы одинаковых символов исходной
# строки заменяются на этот символ и количество его повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку,
# кодирует её предложенным алгоритмом и выводит закодированную последовательность на экран.
# Кодирование должно учитывать регистр символов.

message = input('Введите строку: ')

message_symbols = [sym for sym in message]
message_symbols.append('^')

new_message = ''

sym_count = 1
for i_sym in range(len(message_symbols) - 1):
    if message_symbols[i_sym + 1] == message_symbols[i_sym]:
        sym_count += 1
    else:
        new_message += ''.join([message_symbols[i_sym], str(sym_count)])
        sym_count = 1

print('Результат: {}'.format(new_message))

