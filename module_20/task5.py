# В одной базе данных хранится информация о членах нескольких разных семей.
# Хранение реализовано с помощью словаря с парами «Ф. И. — возраст».
#
# Напишите программу, которая запрашивает у пользователя фамилию и выводит на экран возраст всех членов одной семьи.
# Учтите, что, например, у двух людей разного пола фамилии различаются окончаниями.
# Поиск не должен быть регистрозависимым.


people_dict = {
    ('Бабаев', 'Эмиль'): 23,
    ('Бабаев', 'Самир'): 44,
    ('Бабаева', 'Сабина'): 44,
    ('Байдиков', 'Александр'): 19,
    ('Байдикова', 'Ксения'): 17,
    ('Меликов', 'Зейнал'): 24,
    ('Меликова', 'Сабина'): 39
}

surname = input('Введите фамилию: ').capitalize()

for key, value in people_dict.items():
    if key[0].startswith(surname):
        print('{name} {surname} {age}'.format(
            name=key[1],
            surname=key[0],
            age=value
        ))
