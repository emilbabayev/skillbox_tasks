# Для турнира по волейболу необходимо сформировать турнирную сетку из восьми человек на два дня.
# На первый день из списка участников решили выбрать каждого второго.
# Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар.

# Напишите программу, которая выводит элементы списка только с чётными индексами.

players = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

for i in range(1, len(players), 2):
    print(players[i])

