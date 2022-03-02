chat = list()


def show_chat():
    for el in chat:
        name, message = el
        print(f'{name}: {message}')
    print()


while True:
    user_name = input('Имя пользователя: ')
    print('1.Посмотреть текущий текст чата.\n'
          '2.Отправить сообщение')
    try:
        action = int(input())
        if action != 1 and action != 2:
            raise ValueError

        if action == 1:
            show_chat()

        elif action == 2:
            user_message = input('Сообщение: ')
            if user_message:
                chat.append((user_name, user_message))
            else:
                print('Сообщение не может быть пустым')
                continue

    except ValueError:
        print('Пожалуйста, введите 1 или 2\n')
        continue
