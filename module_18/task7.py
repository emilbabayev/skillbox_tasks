# При написании клиент-серверного приложения часто приходится работать с теми самыми IP-адресами.
# Как мы уже знаем, IP-адрес состоит из четырёх целых чисел в диапазоне от 0 до 255, разделённых точками.
#
# Пользователь вводит строку. Напишите программу, которая определяет,
# является ли заданная строка правильным IP-адресом.
# Обеспечьте контроль ввода, где предусматривается ввод целых чисел от 0 до 255, а также точки между ними.


ip_address_numbers = input('Введите IP-адрес: ').split('.')

if len(ip_address_numbers) != 4:
    print('IP-адрес введен не верно. Не хватает чисел: {}'.format(4 - len(ip_address_numbers)))

else:
    for number in ip_address_numbers:
        if not number.isdigit():
            print('{} не является целым числом'.format(number))
            break
        elif not (0 <= int(number) <= 255):
            print('{} не входит в допустимый диапазон [0, 255]'.format(number))
            break
    else:
        ip_address = '.'.join(ip_address_numbers)
        print('IP-адрес введен верно')