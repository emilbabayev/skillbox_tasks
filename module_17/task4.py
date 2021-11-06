# Дана строка, в которой хранятся первые семь букв английского алфавита.
#
# alphabet = 'abcdefg'
#
# Напишите программу, которая выводит на экран 10 вот таких результатов:
#
# Копия строки.
# Элементы строки в обратном порядке.
# Каждый второй элемент строки (включая самый первый).
# Каждый второй элемент строки после первого.
# Все элементы до второго.
# Все элементы, начиная с конца до предпоследнего.
# Все элементы в диапазоне индексов от 3 до 4 (не включая 4).
# Последние три элемента строки.
# Все элементы в диапазоне индексов от 3 до 4 (не включая 5).
# То же, что и в предыдущем пункте, но в обратном порядке.

# Для получения и вывода результатов используйте только команду print и срезы.

alphabet = 'abcdefg'

print('Копия строки:', alphabet[:])
print('Элементы строки в обратном порядке:', alphabet[::-1])
print('Каждый второй элемент строки(включая первый):', alphabet[::2])
print('Все элементы до второго:', alphabet[:3])
print('Все элементы, начиная с конца до предпоследнего:', alphabet[-1:-3:-1])
print('Все элементы в диапазоне индексов от 3 до 4 (не включая 5):', alphabet[3:5])
print('То же, что и в предыдущем пункте, но в обратном порядке:', alphabet[4:2:-1])
