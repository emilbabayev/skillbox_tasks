# Мы уже помогали Степану с реализацией телефонной книги (контактов) на телефоне, однако внезапно оказалось,
# что книге не хватает ещё одной очень полезной функции: поиска!
#
# Напишите программу, которая бесконечно запрашивает у пользователя действие, которое он хочет совершить:
# добавить контакт или найти человека в списке контактов по фамилии.
#
# Действие «Добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер телефона,
# добавляет их в словарь и выводит на экран текущий словарь контактов.
# Если этот человек уже есть в словаре, то выведите соответствующее сообщение.
#
# Действие «Поиск человека по фамилии»: программа запрашивает фамилию и выводит
# все контакты с такой фамилией и их номера телефонов. Поиск не должен зависеть от регистра символов.

phonebook_dict = dict()

while True:

    action = input('Добавить/Поиск: ').lower()
    if action == 'добавить':
        name, surname = input('Введите имя: ').capitalize(), input('Введите фамилию: ').capitalize()
        if (surname, name) in phonebook_dict.keys():
            print('{surname} {name} уже есть в телефонной книжке'.format(
                surname=surname,
                name=name
            ))
        else:
            phone_number = input('Введите номер телефона: ')
            phonebook_dict[(surname, name)] = phone_number

        print('\nТелефонная книжка')
        for key, value in phonebook_dict.items():
            print('{0} - {1}'.format(key, value))
        print()

    if action == 'поиск':
        surname = input('Введите фамилию: ').capitalize()
        print()
        hasFind = False
        print('Результаты поиска:')
        for person, number in phonebook_dict.items():
            if person[0].startswith(surname):
                print('{surname} {name} - {number}'.format(
                    surname=person[0],
                    name=person[1],
                    number=number
                ))
                hasFind = True
        if not hasFind:
            print('По запросу "{}" ничего не найдено'.format(surname))
        print()

