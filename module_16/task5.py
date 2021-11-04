# Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен группы Depeche Mode.
# Каждая песня состоит из названия и продолжительности с точностью до долей минут:

# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]
# ]

# Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками.
# И при этом ему важно, сколько времени в сумме эти N песен будут звучать.
# Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен,
# а на экран выводит общее время их звучания.


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_count = int(input('Сколько песен выбрать? '))

if songs_count > len(violator_songs):
    print('В списке всего', len(violator_songs), 'песен')
else:
    duration = 0
    for i_song in range(songs_count):
        while True:
            print('Название', i_song + 1, 'песни: ', end='')
            my_song = input()
            for song in violator_songs:
                if song[0] == my_song:
                    duration += song[1]
                    break
            else:
                print('Такой песни нет в списке')
                continue
            break

print('Общее время звучания песен:', duration)