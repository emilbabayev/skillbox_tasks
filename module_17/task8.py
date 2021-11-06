# N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N.
# Затем по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i до R_i включительно.
# Определите, какие палки остались стоять на месте.
#
# Напишите программу, которая получает на вход количество палок N и количество бросков K.
# Далее идёт K пар чисел L_i, R_i, при этом 1≤ L_i≤ R_i≤ N.
#
# Программа должна вывести последовательность из N символов,
# где j-й символ есть “I”, если j-я палка осталась стоять, или “.”, если j-я палка была сбита.

sticks_count = int(input('Кол-во палок: '))
sticks = ['I' for _ in range(sticks_count)]

throws_count = int(input('Кол-во бросков: '))

throws = [[int(input('L_i: ')) - 1, int(input('R_i: '))] for i in range(throws_count)]

print('Ряд до бросков:\t  ', sticks)

for i_throw in range(len(throws)):
    print('Бросок', i_throw + 1, '. Сбиты палки с номера', throws[i_throw][0] + 1, 'по номер', throws[i_throw][1])
    sticks[throws[i_throw][0]:throws[i_throw][1]] = ['.' for _ in range(throws[i_throw][1] - throws[i_throw][0])]

print('Ряд после бросков:', sticks)