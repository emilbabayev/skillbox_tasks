# Есть список из 10 случайных чисел.
# Напишите программу, которая делит эти числа на пары кортежей внутри списка, и выведите результат на экран.

import random

my_list = [random.randint(0, 100) for _ in range(10)]
print('Изначальный список: {}'.format(my_list))

evens = [num for i_num, num in enumerate(my_list) if i_num % 2 == 0]
odds = [num for i_num, num in enumerate(my_list) if i_num % 2 != 0]

new_list = list()
for element in zip(evens, odds):
    new_list.append(element)

print('Новый список: {}'.format(new_list))
