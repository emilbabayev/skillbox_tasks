import math

earth_volume = 1.08321 * 10 ** 12
planet_radius = float(input('Введите радиус случайной планеты: '))

planet_volume = 4 / 3 * math.pi * planet_radius ** 3

if planet_volume > earth_volume:
    print(f'Объем Земли меньше, чем объем теоретически возможной планеты в {round(planet_volume / earth_volume, 3)} раз')
elif earth_volume > planet_volume:
    print(f'Объем Земли больше, чем объем теоретически возможной планеты в {round(earth_volume / planet_volume, 3)} раз')
