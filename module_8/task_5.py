educational_grant = int(input('Введите ежемесячную стипендию: '))
expenses = int(input('Введите ежемесячные расходы: '))
total_need_money = 0

for month in range(1, 11):
    need_money = expenses - educational_grant
    print(f'{month}-й месяц: траты {expenses} рублей, не хватает {need_money}')
    expenses += expenses * 3 // 100

    total_need_money += need_money

print(f'Сумма денег, которую необходимо получить у родителей: {total_need_money} рублей.')