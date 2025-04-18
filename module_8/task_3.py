reverse_timer = int(input('Введите время для обратного отсчёта (в секундах): '))
print(f'Таймер установлен на {reverse_timer} секунд')

for second in range(reverse_timer, 0, -1):
    print(f'\nОсталось {second} секунд')
    if int(input(f'Введите 1, если еда готова, или 0, чтобы продолжить: ')):
        print(f'Ваша еда готова, можете забрать! Таймер был прерван на {second} секундах.')
        break
else:
    print('Ваша еда готова. Осторожно, горячo!')