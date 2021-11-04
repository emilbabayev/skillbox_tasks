guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
print('Сейчас на вечеринке', len(guests), 'человек:', guests)

decision = ''

while decision != 'Пора спать':
    decision = input('Гость пришел или ушел? ')

    if decision == 'пришел' or decision == 'пришёл' or decision == 'Пришел' or decision == 'Пришёл':
        guest_name = input('Имя гостя: ')
        if guest_name in guests:
            print(guest_name, 'уже здесь')
        elif len(guests) >= 6:
            print('Прости, ', guest_name, ', но мест нет', sep='')
        else:
            print('Привет,', guest_name)
            guests.append(guest_name)

    elif decision == 'ушел' or decision == 'ушёл' or decision == 'Ушел' or decision == 'Ушёл':
        guest_name = input('Имя гостя: ')
        if guest_name in guests:
            print('Пока,', guest_name)
            guests.remove(guest_name)
        else:
            print('Такого человека нет на вечеринке')

    else:
        print('Что, простите? ')

print('Вечеринка закончилась.', guests, 'легли спать')