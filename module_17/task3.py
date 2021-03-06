# Мы хотим протестировать работу электронной таблицы для участников некоторых соревнований.
# Есть два списка (то есть две команды), по 20 участников в каждом.
# В этих списках хранятся очки каждого участника (это вещественные числа с двумя знаками после точки, например 4.03).
# Участник одной команды соревнуется с участником другой команды под таким же номером.
# То есть первый соревнуется с первым, второй — со вторым и так далее.
#
# Напишите программу, которая генерирует два списка участников (по 20 элементов)
# из случайных вещественных чисел (от 5 до 10). Для этого найдите подходящую функцию из модуля random.
# Затем сгенерируйте третий список, в котором окажутся только победители из каждой пары.

import random

team1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [team1[i] if team1[i] > team2[i] else team2[i] for i in range(20)]

print('Первая команда:', team1)
print('Вторая команда:', team2)
print('Победители:', winners)