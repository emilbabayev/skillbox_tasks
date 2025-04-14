player_exp = int(input('Введите количество опыта: '))
player_lvl = 1

if 1000 <= player_exp < 2500:
    player_lvl = 2
elif 2500 <= player_exp < 5000:
    player_lvl = 3
elif player_exp >= 5000:
    player_lvl = 4


print(f'Уровень: {player_lvl}')