# Одна библиотека поручила вам написать программу для оцифровки словарей слов-синонимов.
# На вход в программу подаётся N пар слов. Каждое слово является синонимом к парному ему слову.
#
# Реализуйте код, который составляет словарь слов-синонимов (все слова в словаре различны),
# затем запрашивает у пользователя слово и выводит на экран его синоним.
# Обеспечьте контроль ввода: если такого слова нет, то выведите ошибку и запросите слово ещё раз.
# При этом проверка не должна зависеть от регистра символов.

words_couple_count = int(input('Кол-во пар слов: '))
synonym_dict = dict()

for _ in range(words_couple_count):
    print('Введите 2 слова (синонимы):')
    synonym_dict[input('2: ').lower().strip()] = input('1: ').lower().strip()


while True:
    search_word = input('\nПоиск слова: ')
    if search_word in synonym_dict:
        print('Синоним к слову {word} - {synonym}'.format(
            word=search_word,
            synonym=synonym_dict.get(search_word)
        ))
        break
    elif search_word in synonym_dict.values():
        print('Синоним к слову {word} - {synonym}'.format(
            word=search_word,
            synonym=list(synonym_dict.keys())[list(synonym_dict.values()).index(search_word)]
        ))
        break

    print('Слова {word} нет в словаре'.format(word=search_word))
