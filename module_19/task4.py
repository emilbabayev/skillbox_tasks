# Напишите программу, которая рассчитывает,
# на какую сумму лежит каждого товара на складе, и выводит эту информацию на экран.

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}


store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],

    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],

    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],

    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for item in store.keys():
    total_quantity = 0
    total_price = 0
    for purchase in store[item]:
        total_quantity += purchase.get('quantity')
        total_price += purchase.get('price') * purchase.get('quantity')
    print('{item} - {total_quantity} штук, стоимость {total_price} руб.'.format(
        item=list(goods.keys())[list(goods.values()).index(item)],
        total_quantity=total_quantity,
        total_price=total_price
    ))

