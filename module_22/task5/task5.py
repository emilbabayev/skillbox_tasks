import os

text = input('Введите строку: ')

folders_list = input('Куда хотите сохранить документ? '
                     'Введите последовательность папок (через пробел):\n').split()
folder_path = os.path.sep.join(folders_list)

if not os.path.exists(folder_path):
    print('Такого пути не существует')

else:
    file_name = input('Введите имя файла: ')

    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(file_path):
        f = open(file_path, 'w')
        f.write(text)
        print('Файл успешно сохранен!')
        f.close()
    else:
        print(f'Файл {file_name} уже существует. Вы действительно хотите перезаписать файл? ', end='')
        answer = input()
        if answer.lower() == 'да':
            f = open(file_path, 'w')
            f.write(text)
            print('Файл успешно перезаписан!')
            f.close()