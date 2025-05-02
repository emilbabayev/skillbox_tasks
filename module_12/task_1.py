def summa_n(num):
    result = int((1 + num) / 2 * num)
    print(f'Сумма чисел от 1 до {num} равна {result}')


number = int(input('Введите число N: '))
summa_n(number)