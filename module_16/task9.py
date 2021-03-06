# N друзей постоянно берут в долг друг у друга деньги.
# В какой-то момент им надоело забывать, кто кому и сколько должен, и они придумали систему долговых расписок.
# И чтобы начать новый год «с чистого листа»,
# друзья решили оплатить все долговые расписки, которые накопились у них друг к другу.
# Однако выяснилось, что иногда один и тот же человек в разные дни выступал как в роли должника, так и в роли кредитора.
#
# Напишите программу, которая по заданным распискам вычислит,
# сколько всего должен каждый друг выплатить другим (или получить с других).
# Сначала вводится число N — количество друзей, затем вводится число K — количество долговых расписок,
# после этого следует K троек чисел: номер друга, взявшего в долг, номер друга, давшего деньги, и сумма.
# Гарантируется, что ни один друг не брал в долг сам у себя.
#
# Программа должна вывести «баланс друзей», то есть суммы, которые должны получить или отдать друзья.
# Положительное число означает, что друг должен получить деньги от других, отрицательное — должен отдать деньги.

friends_count = int(input('Кол-во друзей: '))
friends = []
for i in range(1, friends_count + 1):
    friends.append([i, 0])

print(friends)
debt_docs_count = int(input('Долговых расписок: '))

for document in range(debt_docs_count):
    lender = int(input('Кому: '))
    debter = int(input('От кого: '))
    cash = int(input('Сколько: '))
    friends[lender - 1][1] += cash
    friends[debter - 1][1] -= cash
    print()

print('Баланс друзей:')
for friend in friends:
    print(friend[0], ': ', friend[1], sep='')