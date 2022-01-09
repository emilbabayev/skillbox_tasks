# Напишите рекурсивную функцию, которая раскрывает все вложенные списки, то есть оставляет только внешний список.

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18],
                                                     [19], [20, 21, [22, 23, [24]]]]]


def unpack_list(lst, new_list=list()):
    for sub in lst:
        if not isinstance(sub, list):
            new_list.append(sub)
        else:
            unpack_list(sub)

    return new_list


unpacked_list = unpack_list(nice_list)
print(unpacked_list)

