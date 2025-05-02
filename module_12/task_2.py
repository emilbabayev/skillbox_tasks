def test():
    num = int(input('Введите целое число: '))
    if num > 0:
        positive()
    elif num < 0:
        negative()


def positive():
    print('Положительное\n')
    test()


def negative():
    print('Отрицательное\n')
    test()


test()