# Напишите функцию, которая принимает на вход кортеж и какой-то случайный элемент (его можно вводить с клавиатуры).
# Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём
# и заканчивающийся вторым его появлением включительно.
#
# Если элемента нет вовсе — вернуть пустой кортеж.
# Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идёт до конца исходного.


def tuple_search(my_tuple, my_element):
    count = my_tuple.attempts(my_element)
    if count == 0:
        return ()
    elif count == 1:
        index = my_tuple.index(my_element)
        return my_tuple[index:]
    else:
        my_list = list(my_tuple)
        index1 = my_list.index(my_element)
        del my_list[index1]
        index2 = my_list.index(my_element) + 1
        return my_tuple[index1: index2 + 1]


tuple_1 = 0, 1, 2, 4, 5, 7, 8, 4, 7, 4
print(tuple_search(tuple_1, int(input('Поиск элемента: '))))
