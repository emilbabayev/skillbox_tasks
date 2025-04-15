cash_amount = int(input('Вклад в банке: '))
percent = int(input('Проценты: '))
edge = int(input('Порог вклада: '))
year = 1

while cash_amount < edge:
    print(f'{year} год. {cash_amount} + {percent}% = ', end='')
    cash_amount += cash_amount * percent // 100
    print(cash_amount)
    year += 1