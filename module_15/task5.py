# Илья зашёл на один любительский киносайт, где пользователи пишут рецензии на фильмы. Вот, кстати, список этих фильмов:
# Илья на сайте в первый раз,
# он хочет зарегистрироваться и сразу добавить некоторые фильмы
# в список своих любимых, чтобы потом почитать рецензии на них.

# Напишите программу, в которой пользователь вводит фильм, и если он есть в списке, то он добавляется в список любимых.
# Если его нет, то выводится ошибка. В конце выведите весь список любимых фильмов.

anime_list = ['Наруто', 'Блич', 'Токийский гуль', 'Мастера меча онлайн', 'Убийца Акаме', 'Ванпанчмен', 'Тетрадь Смерти']
searched_anime = ''
favorites = []

while True:
    searched_anime = input('Введите аниме: ')
    if searched_anime == 'end':
        print('Всего доброго!')
        break

    for i in range(len(anime_list)):
        if anime_list[i] == searched_anime:
            if anime_list[i] in favorites:
                print('Уже добавлено')
                break
            else:
                print('Аниме добавлено в список избранных')
                favorites.append(searched_anime)
                break
    else:
        print('К сожалению такого аниме нет в списке')

    question = int(input('\nХотите увидеть список избранных? (1-да, 0-нет) '))
    if question == 1:
        print(favorites)
