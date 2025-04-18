debtors_count = int(input('Введите количество должников: '))
total_debt = 0

for debtor in range(0, debtors_count, 5):
    print(f'Должник с номером {debtor}')
    total_debt += int(input('Сколько должны? '))

print(f'Общая сумма долга: {total_debt}')