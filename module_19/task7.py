# В базе данных интернет-магазина PizzaTime хранятся данные
# о том, кто, что и сколько заказывал у них в определённый период.
# Вам нужно структурировать эту информацию, а также понять, сколько всего пицц купил каждый заказчик.
#
# На вход в программу подаётся N заказов.
# Каждый заказ представляет собой строку вида «Покупатель — название пиццы — количество заказанных пицц».
# Реализуйте код, который выводит список покупателей и их заказов по алфавиту.
# Учитывайте, что один человек может заказать одно и то же несколько раз.

orders_count = int(input('Введите кол-во заказов: '))
buyers_dict = dict()


for order in range(orders_count):
    while True:
        print('Заказ #{}\n'
              '(покупатель - название пиццы - количество заказанных пицц)'.format(order + 1))
        order_info = input().split('-')
        order_info = [item.strip() for item in order_info]

        if len(order_info) != 3:
            print('Ошибка ввода')
            continue
        else:
            if not (order_info[0] in buyers_dict.keys()):
                buyers_dict[order_info[0]] = list()
                order = {order_info[1]: order_info[2]}
                buyers_dict[order_info[0]].append(order)
                break
            else:
                order = {order_info[1]: order_info[2]}
                buyers_dict[order_info[0]].append(order)
                break

print()
for buyer in buyers_dict.keys():
    print('Покупатель: {}'.format(buyer))
    for order in buyers_dict.get(buyer):
        for pizza in order.keys():
            print('{pizza} - {count} шт.'.format(
                pizza=pizza,
                count=order[pizza]
            ))
    print()


