code_word = input('Введите зашифрованное сообщение: ')

decode_word_part1 = ''
decode_word_part2 = ''


for sym_id, sym in enumerate(code_word, start=1):
    if sym_id % 2 != 0:
        decode_word_part1 += sym
    else:
        decode_word_part2 = sym + decode_word_part2

print(decode_word_part1 + decode_word_part2)