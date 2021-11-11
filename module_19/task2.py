# Антон помимо программирования также увлекается и географией, поэтому он решил связать эти две области и написать
# для своего проекта небольшую программу-навигатор.
#
# Пользователь вводит количество стран N, а затем N раз вводит страну и города,
# которые в этой стране находятся, в одну строку. Затем пользователь вводит три названия городов.
# Реализуйте такую программу и для каждого из трёх городов укажите, в какой стране он находится.
# Если такого города нет, то выведите соответствующее сообщение.

country_count = int(input('Кол-во стран: '))
countries_info_dict = dict()

for _ in range(country_count):
    country_string = input('Страна и ее города: ').split()
    countries_info_dict[country_string[0]] = country_string[1:]

print(countries_info_dict)

for _ in range(country_count):
    city = input('\nВведите город: ')
    for country in countries_info_dict.values():
        if city in country:
            print('Город {city} находится в {country}'.format(
                city=city,
                country=list(countries_info_dict.keys())[list(countries_info_dict.values()).index(country)]
            ))

