from typing import List

films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист', 

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня', 

    'Проклятый остров', 'Начало', 'Матрица'

]

favs = []

while True:
    searched_film = input('Название фильма: ')

    if searched_film in films:

        while True:
            action = input('Команды: добавить, вставить, удалить\n').lower()

            if action == 'добавить':
                if searched_film in favs:
                    print('Фильм уже добавлен в ваш список')
                    print('Ваш текущий список:', favs)
                    print()
                else:
                    favs.append(searched_film)
                    print('Фильм успешно добавлен')
                    print('Ваш текущий список:', favs)
                    print()
                break

            elif action == 'вставить':
                if searched_film in favs:
                    print('Фильм уже добавлен в ваш список')
                    print('Ваш текущий список:', favs)
                    print()
                else:
                    while True:
                        paste_index = int(input('Укажите место: '))
                        if paste_index > 0:
                            break
                        else:
                            print('Ошибка ввода')
                    favs.insert(paste_index - 1, searched_film)
                    print('Фильм успешно добавлен')
                    print('Ваш текущий список:', favs)
                    print()
                break

            elif action == 'удалить':
                if not(searched_film in favs):
                    print('Такого фильма нет в вашем списке')
                    print('Ваш текущий список:', favs)
                    print()
                else:
                    favs.remove(searched_film)
                    print('Ваш текущий список:', favs)
                    print()
                break

            else:
                print('Такой команды нет. Попробуйте еще раз')
    else:
        print('Такого фильма нет на сайте')