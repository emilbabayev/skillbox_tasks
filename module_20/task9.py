# Первая строка содержит число N — это общее количество строк протокола.
# Каждая из следующих N строк содержит записанные через пробел результат участника (целое неотрицательное число)
# и игровое имя (имя не может содержать пробелов). Строки исходных данных соответствуют строкам протокола
# и расположены в том же порядке, что и в протоколе.
#
# Гарантируется, что в соревнованиях не менее трёх участников.
# Программа должна вывести имена и результаты трёх лучших игроков

players_dict = {}

record_amt = int(input('Сколько записей вносится в протокол? '))

print('Записи (результат и имя): ')
for i_record in range(record_amt):
    record = input(f'{i_record + 1} запись: ').split()
    score, name = record
    score = int(score)
    if players_dict.get(name, 0) < score:
        players_dict[name] = score

players = list(players_dict.items())
sorted_players = sorted(players, key=lambda x: x[1], reverse=True)

print('Итоги соревнований:')
for i_player, player in enumerate(sorted_players[:3]):
    print('{place} место. {player} ({score})'.format(
        place=i_player + 1,
        player=player[0],
        score=player[1]
    ))