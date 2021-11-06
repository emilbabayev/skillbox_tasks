# Дан вот такой (уже многомерный!) список:
#
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# Напишите код, который «раскрывает» все вложенные списки, то есть оставляет только внешний список.
# Для решения используйте только list comprehensions.

nice_list = [[[1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11]], [[12, 13, 14, 15], [16], [17, 18, 19, 20, 21, 22]]]

my_list = [nice_list[i][j][k] for i in range(len(nice_list))
           for j in range(len(nice_list[i]))
           for k in range(len(nice_list[i][j]))
           ]

print('Ответ:', my_list)