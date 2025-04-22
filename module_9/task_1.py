success_count = 0

for count in range(10):
    phrase = input('Введите слово: ')
    if phrase == 'Карамба' or phrase == 'карамба':
        success_count += 1

print(f'На борт попадут {success_count} ч.')