number = int(input('Введите число: '))
result = 0

for divider in range(2, number):
    if number % divider == 0:
        result = divider
        break
else:
    result = number

print('Наименьший делитель, отличный от единицы:', result)