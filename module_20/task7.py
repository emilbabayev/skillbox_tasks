# Напишите функцию, которая сортирует кортеж, состоящий из целых чисел, по возрастанию и возвращает его.
# Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.

def my_tuple_sort(my_tuple):
    for element in my_tuple:
        if not isinstance(element, int):
            return my_tuple

    my_list = list(my_tuple)
    for i_num in range(len(my_list)):
        for j_num in range(len(my_list)):
            if my_list[i_num] < my_list[j_num]:
                my_list[i_num], my_list[j_num] = my_list[j_num], my_list[i_num]

    return tuple(my_list)


tuple_1 = 10, 9, 5, 15, 3, 23892
print('Исходный кортеж: {}'.format(tuple_1))
print('Итоговый кортеж: {}'.format(my_tuple_sort(tuple_1)))

