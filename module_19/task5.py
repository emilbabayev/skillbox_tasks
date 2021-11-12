# Мы уже писали программу для лингвистов, которая получала на вход текст и считала,
# сколько раз в строке встречается каждый символ.
# Теперь задача немного поменялась: максимальную частоту выводить не нужно,
# однако теперь необходимо написать функцию, которая будет инвертировать полученный словарь.
# То есть в качестве ключа будет частота, а в качестве значения — список символов с этой частотой.
# Реализуйте такую программу.

text = input('Введите строку: ')
sym_dict = dict()

for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1

sym_dict_alternative = dict()

for sym in sym_dict.keys():
    if sym_dict[sym] in sym_dict_alternative:
        sym_dict_alternative[sym_dict[sym]].append(sym)
    else:
        sym_dict_alternative[sym_dict[sym]] = list()
        sym_dict_alternative[sym_dict[sym]].append(sym)

print('Оригинальный словарь частот')
for el in sym_dict.keys():
    print('{0}: {1}'.format(el, sym_dict.get(el)))

print()

print('Инвертированный словарь частот:')
for el in sym_dict_alternative.keys():
    print('{0}: {1}'.format(el, sym_dict_alternative.get(el)))