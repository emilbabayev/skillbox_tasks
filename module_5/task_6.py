cost = int(input('Стоимость квартиры: '))
area = int(input('Площадь квартиры: '))

if area >= 100 and cost <= 10000000 or area >= 80 and cost <= 7000000:
    print('Подходит')
else:
    print('Не подходит')