# Частная контора даёт в прокат ролики самых разных размеров.
# Человек может надеть ролики любого размера, которые не меньше размера его ноги.
#
# Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей.
# Реализуйте код, который определяет, какое наибольшее число человек
# сможет одновременно взять ролики и пойти покататься.

skates = []
people = []

skates_count = int(input('Кол-во коньков: '))

for i_skate in range(skates_count):
    skate_size = int(input(f'Размер {i_skate + 1} пары: '))
    skates.append(skate_size)

people_count = int(input('Кол-во людей: '))

for i_people in range(people_count):
    foot_size = int(input(f'Размер ноги {i_people + 1} человека: '))
    people.append(foot_size)

people.sort()
skates.sort()

count = 0
temp = 0
for i_people in range(people_count):
    for j_skate in range(skates_count - temp):
        if people[i_people] <= skates[j_skate]:
            skates.remove(skates[j_skate])
            temp += 1
            count += 1
            break

print('Наибольшее кол-во людей, которые смогут взять ролики:', count)