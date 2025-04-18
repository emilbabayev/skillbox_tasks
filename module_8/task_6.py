boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))

result = ''

if boys > girls * 2 or girls > boys * 2:
    print('Нет решения')
elif boys >= girls:
    diff = boys - girls
    for bgb in range(diff):
        result += ' B G B'
    for bg in range(girls - diff):
        result += ' B G'
else:
    diff = girls - boys
    for gbg in range(diff):
        result += ' G B G'
    for gb in range(boys - diff):
        result += ' G B '

print(result)