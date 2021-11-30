# Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную глубину — уровень,
# до которого будет просматриваться структура.
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран.
# По умолчанию уровень не задан. В качестве примера можно использовать такой словарь:

site = {
    'html': {
        'head': {
            'title': 'Мой сайт',
            'style': 'Мои стили'
        },

        'body': {
            'h1': 'Здесь будет мой заголовок',
            'div': {
                'h2': 'Второй заголовок',
                'blockquote': 'Моя цитата',
                'div2': {
                    'a': 'Здесь ссылка',
                    'h3': 'И последний заголовок'
                }
            },
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_element(struct, key, level=None):
    if key in struct.keys():
        return struct[key]
    for element in struct.values():
        if isinstance(element, dict):
            result = find_element(element, key)
            if result:
                break
    else:
        result = None

    return result


user_search = input('Введите искомый элемент: ')
search_result = find_element(site, user_search)
print('{}: {}'.format(user_search, search_result))
