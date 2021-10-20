# Мы пишем программу — анализатор слов, чтобы потом, возможно,
# использовать её для тренировки нейросети, которая будет генерировать нужный нам текст.
# Пользователь вводит слово.
# Напишите программу, которая считает количество уникальных букв в слове.
# Уникальные буквы — это те, которые встречаются всего один раз.

word = input('Введите слово: ')
sym_list = list(word)
sym_count = []

for i in range(len(sym_list)):
    sym_count.append(True)

for i in range(len(sym_list)):
    for j in range(i + 1, len(sym_list)):
        if sym_list[i] == sym_list[j]:
            sym_count[i] = False
            sym_count[j] = False

counter = 0
for i in range(len(sym_count)):
    if sym_count[i]:
        counter += 1

print('Кол-во уникальных букв:', counter)

