counter = 0
for num in range(1, 11):
    person_id = int(input('Введите номер человека: '))
    if person_id % 2 == 0 and person_id > 0:
        counter += 1

print(f'Количество корректных номер (четных и положительных): {counter}')