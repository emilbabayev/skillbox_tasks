zen_file = open('zen.txt', 'r')

data = zen_file.read()

sym_count = len(data)
word_count = len(data.split())
line_count = len(data.split('\n'))

print(f'Кол-во символов: {sym_count}\n'
      f'Кол-во слов: {word_count}\n'
      f'Кол-во строк: {line_count}')

sym_dict = dict()

for i_sym in data:
    i_sym = i_sym.lower()
    if i_sym in sym_dict:
        sym_dict[i_sym] += 1
    elif i_sym.isalpha():
        sym_dict[i_sym] = 1

least_common_letters = list()
least_appearance = min(sym_dict.values())

for sym, count in sym_dict.items():
    if count == least_appearance:
        least_common_letters.append(sym)

print(f'Меньше всего встречаются символы {least_common_letters}: {least_appearance} раз')



