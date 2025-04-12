points_russian = int(input('Введите количество баллов по русскому языку: '))
points_math = int(input('Введите количество баллов по математике: '))
points_info = int(input('Введите количество баллов по информатике: '))

result = points_russian + points_math + points_info

if result >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')

