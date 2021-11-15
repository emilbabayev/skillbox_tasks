# Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен,
# а на экран выводит общее время их звучания.

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_count = int(input('Сколько песен выбрать: '))

duration = 0
for i_song in range(songs_count):
    while True:
        print('Песня #{}: '.format(i_song + 1), end='')
        song = input('')
        if violator_songs.get(song):
            duration += violator_songs.get(song)
            break
        else:
            print('Такой песни нет в списке')

print('Общая длительность: {}'.format(round(duration, 2)))