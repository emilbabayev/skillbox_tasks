# При регистрации на сайте помимо логина нужно ещё придумать надёжный пароль.
# Этот пароль должен состоять минимум из восьми символов,
# в нём должна быть хотя бы одна большая буква и хотя бы три цифры. Тогда он будет считаться надёжным.
#
# Напишите программу, которая запрашивает у пользователя пароль до тех пор,
# пока он не введёт надежный пароль. Используется латиница.

def is_strong(password):
    flag1 = False
    flag2 = False
    password_symbols = [sym for sym in password]

    for sym in password_symbols:
        if sym.isupper():
            flag1 = True
    else:
        digit_count = 0
        for sym in password_symbols:
            if sym.isdigit():
                digit_count += 1
        if digit_count >= 3:
            flag2 = True

    return flag1 and flag2


my_password = input('Введите пароль: ')
while not is_strong(my_password):
    print('Пароль не достаточно надежный\n')
    my_password = input('Введите пароль: ')

print('Пароль надежный!')