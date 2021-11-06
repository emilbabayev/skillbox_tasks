# Дан список из N целых чисел.
# Напишите программу, которая выполняет «сжатие списка» — переставляет все нулевые элементы в конец массива.
# При этом все ненулевые элементы располагаются в начале массива в том же порядке. Затем все нули из списка удаляются.
import random

num_count = int(input('Кол-во чисел: '))
numbers = [random.randint(0, 2) for _ in range(num_count)]

print('Текущий список чисел:', numbers)

shift = 0
for i_num in range(len(numbers)):
    if numbers[i_num - shift] == 0:
        numbers.remove(0)
        numbers.append(0)
        shift += 1

numbers = numbers[:numbers.index(0)]

print('Окончательный список:', numbers)