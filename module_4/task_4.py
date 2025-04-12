chair_1 = int(input('Стоимость 1го стула: '))
chair_2 = int(input('Стоимость 2го стула: '))
chair_3 = int(input('Стоимость 3го стула: '))

total = chair_1 + chair_2 + chair_3

if total > 10000:
    discount = total * 10 // 100
    total -= discount
    print('\nБыла применена скидка!')

print(f'Итоговая сумма: {total}')