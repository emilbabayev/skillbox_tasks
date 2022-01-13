first_tour_file = open('first_tour.txt', 'r')

players = first_tour_file.read().split('\n')
pass_score = int(players.pop(0))

second_tour_players = dict()

for player in players:
    player_surname = player.split()[0]
    player_name = player.split()[1]
    player_score = int(player.split()[2])

    if player_score > pass_score:
        second_tour_players[player_score] = f'{player_name[0:1]}. {player_surname}'

sorted_scores = sorted(second_tour_players.keys(), reverse=True)

second_tour_info = f'{str(len(second_tour_players))}\n'
for i_score, score in enumerate(sorted_scores):
    second_tour_info += f'{i_score + 1}) {second_tour_players[score]} {score}\n'

second_tour_file = open('second_tour.txt', 'w')
second_tour_file.write(second_tour_info)
second_tour_file.close()