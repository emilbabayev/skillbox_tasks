# Мы пишем программу — анализатор слов, чтобы потом, возможно,
# использовать её для тренировки нейросети, которая будет генерировать нужный нам текст.
# Пользователь вводит слово.
# Напишите программу, которая считает количество уникальных букв в слове.
# Уникальные буквы — это те, которые встречаются всего один раз.

word = input('Введите слово: ')
sym_list = list(word)

check_unique = [True for _ in range(len(sym_list))]

for i in range(len(sym_list)):
    for j in range(i + 1, len(sym_list)):
        if sym_list[i] == sym_list[j]:
            check_unique[i], check_unique[j] = False, False

unique_count = 0
for el in check_unique:
    if el:
        unique_count += 1

print('Кол-во уникальных букв:', unique_count)

